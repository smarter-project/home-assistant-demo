# home-assistant-demo

Home Assistant configured to work with our demos.

This README provides instructions on how to deploy a ready-to-use instance of Home Assistant.

The configuration of HA includes a number of areas and sensors. Most of the sensors are discovered using the MQTT discovery mode.

The instance includes a MQTT broker along with the MQTT and MCP Server integrations.



## Deploy

This version uses kubernetes to deploy the containers. Assuming that you have a kubernetes cluster running, you can use the foloowing scripts:

`up`:  contains the kubectl commands to deploy the various services, volumes and deployements.
`down: contains the kubectl commands to remove everything

Two kubernetes services are used insiode the deployment:

The `home-assistant' service uses port 8123 internally. It is also available externally on port 30123 (on any node on which this has been deployed)

The 'mosquitto' service uses port 1833 internally. It is also available externally on port 31883 (on any node on which this has been deployed)


Once all the containers are running, the web GUI should be available and you should be able to log into Home Assistant

[http://<node-name-or-ip>:30123](http://<node-name-or-ip>:30123)

To login via the GUI use these credentials:

```
Name: vm-user
Password: vm-user
```

The HomeAssistant API api is available at:

[http://<node-name-or-ip>:30123/api](http://<node-name-or-ip>:30123/api)

Use this long-lived API token for authentication:

```API_ACCESS_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0OTA4YzBjZmRlMTg0ZjAyOTE4Zjg4ODdjMzBiNGI4OCIsImlhdCI6MTc0ODUyNzQ4MCwiZXhwIjoyMDYzODg3NDgwfQ.MmXRZ38vUlKNijfYaBEdR_A2MoX7NwY_88lBe1BddfA```


The instance includes an MQTT broker reachable using:
[http://<node-name-or-ip>:31883](http://<node-name-or-ip>:31883)

```
  user: mqtt-user
  password: mqtt-user    
```

The instance includes an MCP Server reachable using: 

[http://<node-name-or-ip>:30123/mcp_server/sse](http://<node-name-or-ip>:30123/mcp_server/sse)

The same long-lived API token shoud be used for authentication.


## Simulate

Once deployed the instance will remain in a static state. A python script is provided in the control directory which can be used to change the state of the various devices within the Home Assistant instance.
This script must be executed within the `data` container that has been deployed.

Example invocation using kubernetes:

`k exec -it <name of data pod> -- /data/control/simulate.py --interval 5 --all --show

This will change the state of all the devices every 5 seconds (some randomness is used to decide whether to change the state of any particular sensor).


Alternatively, the `control/external_simulate.py` script can be run on the node on which the instance is deployed but this would also require the mosquitto-clients package to be installed.

```
./control/external_simulate.py --interval 5 --all --show
```




## Build

Building the image that sets up the initial configuration of the instance:

`docker build -t ha_data_k8s:1.0 .`

The data-deployment.yaml uses a pre-built image at: ```ghcr.io/smarter-project/ha_data_k8s:1.0```




