#!/usr/bin/python3
import os
import subprocess
import time
import json
import random
import re
import argparse

parser = argparse.ArgumentParser(description="Change the state of a device")

# Define arguments
parser.add_argument("--device", required=True, help="Device to control")
parser.add_argument("--state", help="MQTT state topic to set")
parser.add_argument("--command", help="MQTT command topic to set")
parser.add_argument("--show", default=False, help="Show the set/get commands", action='store_true')

# Parse arguments
args = parser.parse_args()

# Access arguments
print("Device:", args.device)
print("State:", args.state)


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
import alarm


def set_state(topic, msg):
    if msg[:5] == "File:":
        if args.show:
            print("Set:", "mosquitto_pub", "-h", BROKER, "-p", PORT, "-u",  USERNAME, "-P", PASSWORD, "-t", topic, "-f", msg[5:])
        subprocess.run(["mosquitto_pub", "-h", BROKER, "-p", PORT, "-u",  USERNAME, "-P", PASSWORD, "-t", topic, "-f", msg[5:]])
    else:
      if args.show:
        print("Set:", "mosquitto_pub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-r", "-t", topic, "-m", msg)
      subprocess.run(["mosquitto_pub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-r", "-t", topic, "-m", msg])

def get_state(topic):
    if args.show:
        print("Get:", "mosquitto_sub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-t", topic, "-C", "1")
    result = subprocess.run(["mosquitto_sub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-t", topic, "-C", "1"], capture_output=True, text=True)
    return result.stdout
    
def get_state(topic):
    result = subprocess.run(["mosquitto_sub", "-h", BROKER, "-u",  USERNAME, "-P", PASSWORD, "-t", topic, "-C", "1"], capture_output=True, text=True)
    return result.stdout


device_re = args.device

count = 0
for key in data.config_topic.keys():
    if key in data.default_state:    
        # look for the topic
        match = re.search(device_re, data.state_topic[key])
        if match:
            count += 1
            print(data.state_topic[key])
            if args.command:
                count +=1 
                set_state(data.command_topic[key], args.command)
                print(data.command_topic[key], " set to ", args.command)
            elif args.state:
                count +=1 
                set_state(data.state_topic[key], args.state)
                print(data.state_topic[key], " set to ", args.state)

if count == 0:
    print("No devices matched")
            
