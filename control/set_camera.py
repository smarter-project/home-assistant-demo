#!/usr/bin/python3
import os
import time
import json
import random
import re
import argparse
from pathlib import Path
import paho.mqtt.client as mqtt
import threading

# MQTT credentials and settings
BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "31883"))

USERNAME = "mqtt-user"
PASSWORD = "mqtt-user"

import data
import camera

show = True

parser = argparse.ArgumentParser(description="Change the state of a device")

parser.add_argument("--camera", help="Which camera")
parser.add_argument("--image", help="Image to use")
parser.add_argument("--show", default=False, help="Show the set/get commands", action='store_true')

# Parse arguments
args = parser.parse_args()

# Access arguments
print("Device:", args.camera)
print("State:", args.image)



    
def set_state(topic, msg):
    """Publish a message to an MQTT topic"""
    # Read file content and publish
    file_path = msg
    with open(file_path, 'rb') as f:
        file_content = f.read()
        if show:
            print(f"Publishing file content: {topic} -> {file_path}")
            client.publish(topic, file_content, retain=True)
            
# Create MQTT client
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
#client.on_connect = on_connect
#client.on_message = on_message
#client.on_disconnect = on_disconnect

# Connect to the broker
if show:
    print(f"Connecting to MQTT broker at {BROKER}:{PORT}")

client.connect(BROKER, PORT, 60)
    
# Start the network loop in a separate thread
client.loop_start()

set_state(args.camera, args.image)

client.loop_stop()

client.disconnect()

