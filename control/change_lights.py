#!/usr/bin/python3
import os
import subprocess
import time
import json
import random
import re
import argparse
from pathlib import Path

# MQTT credentials and settings
BROKER = os.getenv("MQTT_BROKER", "mosquitto")
PORT =   os.getenv("MQTT_PORT", "1883")

USERNAME="mqtt-user"
PASSWORD="mqtt-user"

import data
import lights

show = True


if Path("/data/images").is_dir():
    media_suffix="/data/"
else:
    media_suffix="./"    


def set_state(topic, msg):
    if msg[:5] == "File:":
        if show:
            print("Set:", "mosquitto_pub", "-h", BROKER, "-p", PORT, "-u",  USERNAME, "-P", PASSWORD, "-t", topic, "-f", media_suffix+msg[5:])
        subprocess.run(["mosquitto_pub", "-h", BROKER, "-p", PORT, "-u",  USERNAME, "-P", PASSWORD, "-t", topic, "-f", media_suffix+msg[5:]])
    else:
      if show:
          print("Set:", "mosquitto_pub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-r", "-t", topic, "-m", msg)
      subprocess.run(["mosquitto_pub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-r", "-t", topic, "-m", msg])


def get_state(topic):
    if show:
        print("Get:", "mosquitto_sub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-t", topic, "-C", "1")
    result = subprocess.run(["mosquitto_sub", "-h", BROKER, "-p", PORT, "-u", USERNAME, "-P", PASSWORD, "-t", topic, "-C", "1"], capture_output=True, text=True)
    return result.stdout.rstrip()


while True:

    light_state=get_state("home/livingroom_light/set")

    if light_state == "ON":
        print("ON")
        set_state("home/livingroom/camera1", "File:images/living_room1_light_on.png")
        set_state("home/livingroom/camera2", "File:images/living_room2_light_on.png")
    elif light_state == "OFF":
        print("OFF")
        set_state("home/livingroom/camera1", "File:images/living_room1_light_off.png")
        set_state("home/livingroom/camera2", "File:images/living_room2_light_off.png")
    else:
        print("** UNSURE ***")        

