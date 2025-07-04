#!/bin/sh -fvx


while true; do

    status=$(curl -s -o /dev/null -w "%{http_code}" http://homeassistant:8123/api/)

    if [ "$status" = "200" ] || [ "$status" = "401" ]; then
        echo "Home Assistant is up"
        break
    else
        echo "Home Assistant is down"
    fi

    sleep 5
done

mosquitto_sub -h mosquitto -p 1883 -t '#' -C 1

sleep 2


SCRIPT_DIR=$(dirname "$0")

$SCRIPT_DIR/config.py

tail -f /dev/null
