#!/bin/sh 


while true; do

status=$(curl -s -o /dev/null -w "%{http_code}" http://homeassistant:8123/api/)

if [ "$status" = "200" ] || [ "$status" = "401" ]; then
    echo "Home Assistant is up"
    break
else
  echo "Home Assistant is down"
fi

sleep 20

done


SCRIPT_DIR=$(dirname "$0")

$SCRIPT_DIR/config.py

tail -f /dev/null
