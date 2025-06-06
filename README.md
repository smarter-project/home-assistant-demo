# home-assistant-demo

Home Assistant configured to work with our demos.

This README provides instructions on how to build and deploy a ready-to-use instance of Home Assistant.

The configuration of HA includes a number of areas and sensors. Most of the sensors are discovered using the MQTT discovery mode.

When everything is up and running the home-assistant web-gui is available at:  

http://localhost:8123

The api is available at:

http://localhost:8123/api.

To login via the GUI use these credentials:

Name: vm-user
Password: vm-user

The instance includes an MQTT broker reachable using:
```
  port: 1883
  user: mqtt-user
  password: mqtt-user    
```
The instance includes an MCP Server reachable using: 

```http://localhost:8123/mcp_server/sse```

plus this long-lived API token for authentication:

```API_ACCESS_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0OTA4YzBjZmRlMTg0ZjAyOTE4Zjg4ODdjMzBiNGI4OCIsImlhdCI6MTc0ODUyNzQ4MCwiZXhwIjoyMDYzODg3NDgwfQ.MmXRZ38vUlKNijfYaBEdR_A2MoX7NwY_88lBe1BddfA```

## Build

Build the image that sets up the initial configuration of the instance:

`docker build -t ha_data:1.0 .`

## Deploy

This version uses docker-compose to deploy the containers:

`docker-compose up -d`

Once all the containers are running, the web GUI should be available and you should be able to log into Home Assistant

This deployment uses volumes and so the configuration is persistent between invocations of docker-compose. 

Remove the `ha_config` and `ha_mosquitto` docker volumes to start from initial state again.


## Simulate

Once deployed the instance will remain in a static state. A python script is provided in the control directory which can be used to change the state of the various devices within the Home Assistant instance.

Example invocation:

`control/simulate.py --interval 5 --all`

This will change the state of all the devices every 5 seconds (some randomness is used to decide whether to change the state of any particualr sensor).








