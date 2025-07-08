FROM alpine

RUN mkdir /data
COPY ./mosquitto /mosquitto
COPY ./config /data/config
COPY ./images /data/images
COPY ./control /data/control
COPY ./update_mqtt.sh /data

RUN apk add python3 mosquitto-clients curl py3-paho-mqtt

ENTRYPOINT ["/data/control/wait.sh"]
