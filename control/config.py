#!/usr/bin/python3
import subprocess
import time
import json
from pathlib import Path

# MQTT credentials and settings
BROKER="localhost"
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
import siren
import presence
import alarm


if Path("/data/media").is_dir():
    media_suffix="/data/"
else:
    media_suffix="./"    
    print("Directory does not exist")


# Add the devices
for key in data.config_topic.keys():
    if key in data.config_msg:
        print("Adding: ", key)
        subprocess.run(["mosquitto_pub", "-h", BROKER, "-u",  USERNAME, "-P", PASSWORD, "-t", data.config_topic[key], "-m", data.config_msg[key]])
    else:
        print("No config for: ", key)

time.sleep(2)
# Setup the default state
for key in data.config_topic.keys():        
    if key in data.default_state:
        s = data.default_state[key]
        print("setting default state of ",key, " to ", s)
        if s[:5] == "File:":
            subprocess.run(["mosquitto_pub", "-h", BROKER, "-u",  USERNAME, "-P", PASSWORD, "-t", data.state_topic[key], "-f", media_suffix+s[6:]])
        else:
            subprocess.run(["mosquitto_pub", "-h", BROKER, "-u",  USERNAME, "-P", PASSWORD, "-r", "-t", data.state_topic[key], "-m", data.default_state[key]])
    else:
        print("no default state")
        


