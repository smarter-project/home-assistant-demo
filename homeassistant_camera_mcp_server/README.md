# home-assistant camera MCP server

Deployable MCP Server that provdes access to cameras in the demo Home Assistant instance.

This README provides instructions on how to deploy and build the MCP server.

# Function


This MCP Server provides two tools:

`get_cameras`: no arguments

Returns a list of the cameras connected to the HomeAssistant instance

`capture`: 

Takes a snapshot using the specified camera and saves it into a file in /images/<camera_id>.jpg. 
A persistent volume is used to share the snapshots with other deployed workloads (such as the face recognition MCP server)


## Deploy

The YAML file: ha_camera_mcp.yaml is used to deploy the server:

```kubectl apply -f ha_camera_mcp.yaml```

It exposes the MCP server on the node port 30900 and internally within k8s on port 9000

Add this entry to the mcp.json configuration file to allow a chat agent to connect to the MCP server and use the tools:

```
    "Home Assistant Cameras": {
      "url": "http://localhost:30900/mcp"
    },
```

The MCP server tries to connect to Home Assistant (within k8s) using port ```8123```and uses this long-lived API token for authentication:

```API_ACCESS_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0OTA4YzBjZmRlMTg0ZjAyOTE4Zjg4ODdjMzBiNGI4OCIsImlhdCI6MTc0ODUyNzQ4MCwiZXhwIjoyMDYzODg3NDgwfQ.MmXRZ38vUlKNijfYaBEdR_A2MoX7NwY_88lBe1BddfA```


## Build

Building the image:

`docker build -t ha_camera_mcp:1.0 .`


The deployment yaml uses a pre-built image at: ```atg-attk--edgeaidocker.artifactory.arm.com/homeassistant-camera-mcp:latest```




