# home-assistant-demo

Deployable Home Assistant configured for Edge AI demonstration.

This README provides instructions on how to deploy a ready-to-use instance of Home Assistant.

This configuration of Home Assistant includes a number of areas and sensors. Most of the sensors are discovered using the MQTT discovery mode.

The instance includes a MQTT broker along with the MQTT and MCP Server integrations.


## Deploy

Kubernetes is used to deploy the everything. Assuming that you have a kubernetes cluster running, you can use the foloowing scripts:

`up`:  contains the kubectl commands to deploy the various services, volumes and deployments.

`down`: contains the kubectl commands to remove everything.

Two kubernetes services are used inside the deployment:

The `home-assistant' service uses port 8123 internally. It is also available externally on port 30123 (on any node on which this has been deployed)

The 'mosquitto' service uses port 1833 internally. It is also available externally on port 31883 (on any node on which this has been deployed)

Two Persistent Volumes are used to provide configuration for msoquitto and Home Assistant.

Once all the containers are running, the web GUI should be available and you should be able to log into Home Assistant

`localhost` can be replaced with the name or IP address of the node on which the pods are running


[http://localhost:30123](http://localhost:30123)

To login via the GUI use these credentials:
```
Name: vm-user
Password: vm-user
```

The HomeAssistant API api is available at:

[http://localhost:30123/api](http://localhost:30123/api)

Use this long-lived API token for authentication:

```API_ACCESS_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0OTA4YzBjZmRlMTg0ZjAyOTE4Zjg4ODdjMzBiNGI4OCIsImlhdCI6MTc0ODUyNzQ4MCwiZXhwIjoyMDYzODg3NDgwfQ.MmXRZ38vUlKNijfYaBEdR_A2MoX7NwY_88lBe1BddfA```


The instance includes an MQTT broker reachable using:
[http://localhost:31883](http://localhost:31883)

```
  user: mqtt-user
  password: mqtt-user    
```

The instance includes an MCP Server reachable using: 

[http://localhost:30123/mcp_server/sse](http://localhost:30123/mcp_server/sse)

The same long-lived API token shoud be used for authentication.


## Simulate

Once deployed the instance will remain in a static state. A python script is provided in the control directory which can be used to change the state of the various devices within the Home Assistant instance.

Two versions of the script are provided in the control directory: `simulate.py` and `external_simulate.py`

The scripts have the same functionality however `external_simulate.py` uses the external ports to communicate with Home Assistant and the MQTT Broker. `external_simulate.py` also requires the MQTT Broker mosquitto clients (mosquitto_pub and mosquitto_sub) to be installed locally. 

Linux (Ubuntu):

    sudo apt install mosquitto-clients

macos:

    brew install mosquitto-clients



The `simulate.py` script is designed to be executed inside the deployed `data` container and uses the internal service names and ports.

Environment variables MQTT_BROKER and MQTT_PORT can be used to override the default name and ports.

### Example invocation using kubernetes:

`kubectl exec -it <name of data pod> -- /data/control/simulate.py --interval 5 --all --show`

This will change the state of all the devices every 5 seconds (some randomness is used to decide whether to change the state of any particular sensor).

### Example local invocation

`control/simulate.py --interval 5 --all --show`

These scripts can be used to change the state of lights (ON/OFF), temperature sensors (varying between 15-26°C) and motion sensors (DETECTED/CLEAR)


## Build

Building the image that sets up the initial configuration of the instance:

`docker build -t ha_data_k8s:1.0 .`

The data-deployment.yaml uses a pre-built image at: ```ghcr.io/smarter-project/ha_data_k8s:1.0```




