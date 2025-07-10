#!/bin/sh -fvx


HOST="mosquitto"
PORT=1883

echo "Waiting for MQTT broker at $HOST:$PORT..."

while ! nc -z "$HOST" "$PORT" >/dev/null 2>&1; do
    echo "MQTT broker not available yet. Retrying in 2 seconds..."
    sleep 2
done

echo "MQTT broker is now running at $HOST:$PORT."

sleep 2


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


SCRIPT_DIR=$(dirname "$0")

$SCRIPT_DIR/config.py

if [ ! -z "$SIMULATE" ]; then 
  MQTT_BROKER=mosquitto MQTT_PORT=1883 $SCRIPT_DIR/change_lights.py /var/log/light.log 2>&1 &
  MQTT_BROKER=mosquitto MQTT_PORT=1883 $SCRIPT_DIR/external_simulate.py --interval 10 --temperature --motion --presence > /var/log/sim.log 2>&1 &
  MQTT_BROKER=mosquitto MQTT_PORT=1883 $SCRIPT_DIR/rotate_camera  > /var/log/cam.log 2>&1 &
fi

tail -f /dev/null

                      
