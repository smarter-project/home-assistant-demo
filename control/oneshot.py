#!/usr/bin/python3
import subprocess
import time
import json
import random
import re
import argparse

parser = argparse.ArgumentParser(description="Turn on a light")

# Define arguments
parser.add_argument("--device", help="Device to control")
parser.add_argument("--state", help="MQTT state topic to set")
parser.add_argument("--command", help="MQTT command topic to set")

# Parse arguments
args = parser.parse_args()

# Access arguments
print("Device:", args.device)
print("State:", args.state)


# MQTT credentials and settings
BROKER="mosquitto"
PORT="1883"
USERNAME="mqtt-user"
PASSWORD="mqtt-user"

import data
import lights
import windows
import temperature
import door
import motion
import camera
import alarm

def set_state(topic, msg):
    subprocess.run(["mosquitto_pub", "-h", BROKER, "-u",  USERNAME, "-P", PASSWORD, "-r", "-t", topic, "-m", msg])

def set_command(topic, msg):
    subprocess.run(["mosquitto_pub", "-h", BROKER, "-u",  USERNAME, "-P", PASSWORD, "-r", "-t", topic, "-m", msg])
    
def get_state(topic):
    result = subprocess.run(["mosquitto_sub", "-h", BROKER, "-u",  USERNAME, "-P", PASSWORD, "-t", topic, "-C", "1"], capture_output=True, text=True)
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


device_re = args.device

count = 0
for key in data.config_topic.keys():
    if key in data.config_msg:
        dd = json.loads(data.config_msg[key])
        
        # look for the topic
        match = re.search(device_re, dd["state_topic"])
        if match:
            if args.command:
                count +=1 
                set_command(dd["command_topic"], args.command)
                print(dd["command_topic"], " set to ", args.command)
            elif args.state:
                count +=1 
                set_state(dd["state_topic"], args.state)
                print(dd["state_topic"], " set to ", args.state)

if count == 0:
    print("No devices matched")
            
