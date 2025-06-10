# home-assistant-demo

Home Assistant configured to work with our demos.

This README provides instructions on how to build and deploy a ready-to-use instance of Home Assistant.

The configuration of HA includes a number of areas and sensors. Most of the sensors are discovered using the MQTT discovery mode.

When everything is up and running the home-assistant web-gui is available at:  

http://localhost:30123

To login via the GUI use these credentials:

Name: vm-user
Password: vm-user

The api is available at:

http://localhost:8123/api

Use this long-lived API token for authentication:

```API_ACCESS_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0OTA4YzBjZmRlMTg0ZjAyOTE4Zjg4ODdjMzBiNGI4OCIsImlhdCI6MTc0ODUyNzQ4MCwiZXhwIjoyMDYzODg3NDgwfQ.MmXRZ38vUlKNijfYaBEdR_A2MoX7NwY_88lBe1BddfA```


The instance includes an MQTT broker reachable using:
```
  port: 31883
  user: mqtt-user
  password: mqtt-user    
```

The instance includes an MCP Server reachable using: 

```http://localhost:8123/mcp_server/sse```


## Build

Build the image that sets up the initial configuration of the instance:

`docker build -t ha_data_k8s:1.0 .`

## Deploy

This version uses kubernetes to deploy the containers. Two scripts are provided that contain the kubectl commands to deply the various services, volumes and deployements.

`up`:  contains the kubectl commands to deploy the various services, volumes and deployements.
`down: contains the kubectl commands to remove everything


Once all the containers are running, the web GUI should be available and you should be able to log into Home Assistant


## Simulate

Once deployed the instance will remain in a static state. A python script is provided in the control directory which can be used to change the state of the various devices within the Home Assistant instance.

Example invocation:

`control/simulate.py --interval 5 --all`

This will change the state of all the devices every 5 seconds (some randomness is used to decide whether to change the state of any particular sensor).








