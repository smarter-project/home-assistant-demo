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
import lights

show = True

if Path("/data/images").is_dir():
    media_suffix = "/data/"
else:
    media_suffix = "./"

# Global variable to store the current light state
current_light_state = None
state_lock = threading.Lock()

def on_connect(client, userdata, flags, rc):
    """Callback for when the client connects to the MQTT broker"""
    if rc == 0:
        if show:
            print("Connected to MQTT broker")
        # Subscribe to the light state topic
        client.subscribe("home/livingroom_light/set")
        if show:
            print("Subscribed to home/livingroom_light/set")
    else:
        print(f"Failed to connect to MQTT broker, return code {rc}")

def on_message(client, userdata, msg):
    """Callback for when a message is received"""
    global current_light_state
    
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    
    if show:
        print(f"Received message: {topic} -> {message}")
    
    if topic == "home/livingroom_light/set":
        with state_lock:
            current_light_state = message
        process_light_state_change(message)

def on_disconnect(client, userdata, rc):
    """Callback for when the client disconnects"""
    if show:
        print("Disconnected from MQTT broker")

def process_light_state_change(light_state):
    """Process light state changes and update camera images"""
    if light_state == "ON":
        print("Light is ON")
        set_state("home/livingroom/camera1", "File:images/living_room1_light_on.jpg")
        set_state("home/livingroom/camera2", "File:images/living_room2_light_on.jpg")
        print("DONE")
    elif light_state == "OFF":
        print("Light is OFF")
        set_state("home/livingroom/camera1", "File:images/living_room1_light_off.jpg")
        set_state("home/livingroom/camera2", "File:images/living_room2_light_off.jpg")
        print("DONE")        
    else:
        print(f"** UNKNOWN STATE: {light_state} ***")

def set_state(topic, msg):
    """Publish a message to an MQTT topic"""
    if msg.startswith("File:"):
        # Read file content and publish
        file_path = media_suffix + msg[5:]
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()
            if show:
                print(f"Publishing file content: {topic} -> {file_path}")
            client.publish(topic, file_content, retain=True)
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
    else:
        if show:
            print(f"Publishing: {topic} -> {msg}")
        client.publish(topic, msg, retain=True)

def get_current_light_state():
    """Get the current light state (thread-safe)"""
    with state_lock:
        return current_light_state

# Create MQTT client
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Connect to the broker
if show:
    print(f"Connecting to MQTT broker at {BROKER}:{PORT}")

try:
    client.connect(BROKER, PORT, 60)
    
    # Start the network loop in a separate thread
    client.loop_start()
    
    # Wait for initial connection and state
    print("Waiting for initial light state...")
    
    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
            # Optional: You can add periodic checks or other logic here
            
    except KeyboardInterrupt:
        print("\nShutting down...")
        
finally:
    client.loop_stop()
    client.disconnect()

