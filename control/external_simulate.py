#!/usr/bin/python3
import os
import subprocess
import time
import json
import random
import re
import argparse

# MQTT credentials and settings
BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT =   os.getenv("MQTT_PORT", "31883")

USERNAME="mqtt-user"
PASSWORD="mqtt-user"

import data
import lights
import windows
import temperature
import door
import motion
import camera


parser = argparse.ArgumentParser(description="Simulate events on HA demo")

# Define arguments
parser.add_argument("--interval", default="5", type=int, help="Time in seconds between entire rounds of state updates")
parser.add_argument("--light",  default=False, help="Include lights in simulation", action='store_true')
parser.add_argument("--temperature", default=False, help="Include temperature sensors in simulation", action='store_true')
parser.add_argument("--motion", default=False, help="Include motion sensors in simulation", action='store_true')
parser.add_argument("--presence", default=False, help="Include presence sensors in simulation", action='store_true')
parser.add_argument("--all", default=False, help="Include all devices simulation", action='store_true')
parser.add_argument("--show", default=False, help="Show the set/get commands", action='store_true')

# Parse arguments
args = parser.parse_args()

if args.all and (args.light or args.temperature or args.motion or args.presence):
    print("Cannot specify -all with other selections")
    exit(1)

if not args.all and not (args.light or args.temperature or args.motion or args.presence):
    print("Must specify --all or other selections")
    exit(1)

def set_state(topic, msg):
    if args.show:
        print("Set:", "mosquitto_pub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-r", "-t", topic, "-m", msg)
    subprocess.run(["mosquitto_pub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-r", "-t", topic, "-m", msg])

def get_state(topic):
    if args.show:
        print("Get:", "mosquitto_sub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-t", topic, "-C", "1")
    result = subprocess.run(["mosquitto_sub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-t", topic, "-C", "1"], capture_output=True, text=True)
    return result.stdout

def wiggle_temperature(i):
    l = temp_rng.random()
    if l > 0.75:
        i = i + 0.2
    elif l < 0.25:
        i = i - 0.2

    if i<15:
        i = 17.6

    if i> 26:
        i = 18.5

    return i


temp_re = r"temperature"
temp_rng= random.Random(41)


light_re = r"light"
light_rng= random.Random(41)


motion_re = r"motion"
motion_rng= random.Random(41)


while True:

    for key in data.config_topic.keys():
        if key in data.config_msg:
            dd = json.loads(data.config_msg[key])

            if args.temperature or args.all:
                # temperature sensors            
                match = re.search(temp_re, dd["state_topic"])
                if match:
                    a = get_state(dd["state_topic"])
                    f = wiggle_temperature(float(a))
                    set_state(dd["state_topic"], f"{f:.1f}")


            if args.light or args.all:                    
                # light sensors
                match = re.search(light_re, dd["state_topic"])
                if match:
                    l = light_rng.random()
                    if l > 0.5:
                        state = "ON"
                    else:
                        state = "OFF"
                        
                    set_state(dd["state_topic"], state)

            if args.motion or args.all:                    
                # motion sensors
                match = re.search(motion_re, dd["state_topic"])
                if match:
                    l = motion_rng.random()
                    if l > 0.9:
                        state = "OPEN"
                    else:
                        state = "CLOSED"
                   
                    set_state(dd["state_topic"], state)
                
    time.sleep(args.interval)
