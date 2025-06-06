# home-assistant-demo

Home Assistant configured to work with our demos.

This README provides instructions on how to build and deploy a ready-to-use instance of Home Assistant.

The configuration of HA includes a number of areas and sensors. Most of the sensors are discovered using the MQTT discovery mode.

When everything is up and running the home-assistant api is available on http://localhost:8123/api.

The web-gui is available at:  http://localhost:8123

The only user provided is: vm-user (password is vm-user)


## Build

Build the image that setus the initial configuration of the instance:

`docker build -t ha_data:1.0 .`

## Deploy

This version uses docker-compose to deploy the containers:

`docker-compose up -d`

Once all the containers are running, the web GUI should be available and you should be able to log into Home Assistant


## Simulate

Once deployed the instance will remain static state. A python script is provided in the control directory which can be used to change the state of the various devices with the Home Assistant instance.

Example invocation:

`control/simulate.py --interval 5 --all`

This will potentially the state of all the devices every 5 seconds. Some randomness is used to decide whether to change the state of any particualr sensor.








