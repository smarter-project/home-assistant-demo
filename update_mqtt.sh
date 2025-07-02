#!/bin/sh -fvx

MQTT=${MQTT_HOST:-mosquitto}

FILE=/shared/config/.storage/core.config_entries

if [ -f ${FILE}.bak ]; then
  F=${FILE}.bak 
  echo "Using backup"
else
  cp ${FILE} ${FILE}.bak
  F=${FILE}.bak     
fi

sed -e "s/mosquitto2/$MQTT/" ${F} > ${FILE}
