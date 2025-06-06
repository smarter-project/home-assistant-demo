#!/bin/sh 


while true; do

status=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8123/api/)

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

tail -f /dev/null
