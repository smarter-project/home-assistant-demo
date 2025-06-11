FROM alpine

RUN mkdir /data
COPY ./mosquitto /mosquitto
COPY ./config /data/config
COPY ./images /data/images
COPY ./control /data/control


RUN apk add python3 mosquitto-clients curl

ENTRYPOINT ["/data/control/wait.sh"]
