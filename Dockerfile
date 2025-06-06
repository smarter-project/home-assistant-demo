FROM alpine

RUN mkdir /data
COPY ./mosquitto /data/mosquitto
COPY ./config /data/config
COPY ./media /data/media
COPY ./control /data/control


RUN apk add python3 mosquitto-clients curl

ENTRYPOINT ["/data/control/wait.sh"]
