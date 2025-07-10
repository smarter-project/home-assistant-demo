# home-assistant-demo

Deployable Home Assistant configured for Edge AI demonstration.

This file provides instructions on how to deploy a ready-to-use instance of Home Assistant.

This configuration of Home Assistant includes a number of areas and sensors. Most of the sensors are discovered using the MQTT discovery mode.

A number of MCP servers can also be deployed which provide tools that can be called from within an LLM-enabled chat.


## Deploy the Home Assistant

Kubernetes is used for deployment. Assuming that you have a kubernetes cluster running, you can use the following scripts:

`up`:  contains the kubectl commands to deploy the various services, volumes and deployments.

`down`: contains the kubectl commands to remove everything.


To login into the HomeAssisant GUI use these credentials:
```
Name: vm-user
Password: vm-user
```
at [http://localhost:30123](http://localhost:30123)


The integrated Home Assistant MCP Server is enabled.


## Deploy the MCP servers and Triton Inference server

`face_up`:  contains the kubectl commands to deploy the various services, volumes and deployments for the MCP servers.

`face_down`:  contains the kubectl commands to remove the various services, volumes and deployments associated with the MCP servers.


Two MCP servers are provided:

`homeassistant_camera_mcp_server` which has two tools: `get_cameras` and `capture`

`face_detection_mcp_server` which has a single tool: `identify_faces`

These two MCP servers share a common mounted volume so that images captured by the camera MCP server can be processed by the face recognition MCP server.

The mcp.json file can be used to configure a tool such as Void/Cursor or LMStudio to connect to the MCP servers.



## Simulation

The default behvaiour for the system can be controlled by an environment variable specified in the `data-deployment.yaml` file.
If the SIMULATE environment variable is set (to anything) then the state of sensors will be continually varied whilst the instance is running. This includes temperature, motion and presence sensors. The images captured by the front camera will also be varied.


