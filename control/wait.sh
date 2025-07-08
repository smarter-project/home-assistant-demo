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

MQTT_BROKER=mosquitto MQTT_PORT=1883 $SCRIPT_DIR/external_simulate.py --interval 10 --temperature --motion --presence > /var/log/mylog.log 2>&1 &

MQTT_BROKER=mosquitto MQTT_PORT=1883 $SCRIPT_DIR/change_lights.py

