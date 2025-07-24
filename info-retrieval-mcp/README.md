# Information Retrieval MCP Server

A FastMCP-based server that manages information retrieval for Home Assistant via MQTT and ServiceDB. This service subscribes to various MQTT topics, captures updates, and provides MCP tools for querying information from different Home Assistant modules.

## Features

- **MQTT Information Subscription**: Automatically subscribes to various topics from Home Assistant modules
- **Real-time Information Updates**: Captures state changes and forwards to ServiceDB
- **MCP Query Tools**: Provides tools for querying information status and historical records
- **Background Processing**: Runs monitoring in background threads
- **ASGI Support**: Production-ready deployment with Gunicorn and Uvicorn
- **Extensible Architecture**: Designed to support multiple Home Assistant modules

## Information Types Supported

- **Sensors**: Lights, temperature, motion, doors, windows, presence sensors
- **Future Modules**: Camera data, device status, automation states, and more

## Requirements

- Python 3.12
- [mcp[cli]](https://github.com/mcp-cli) (v1.10.1+)
- paho-mqtt (v1.6.1+)
- uvicorn (v0.35.0+)
- gunicorn (v21.2.0+)

## Installation

1. **Running in Docker**

   ```bash
   docker build -t local_mw/edge_ai/info-retrieval-mcp:latest .
   docker run --rm -it --name info-mcp -p 7006:7001 -e DANGEROUSLY_OMIT_AUTH=true -e MQTT_BROKER=mosquitto -e MQTT_PORT=1883 local_mw/edge_ai/info-retrieval-mcp:latest
   ```

2. **Example cursor mcp.json**

   ```json
   {
        "mcpServers": {
            "info_retrieval": {
                "url": "http://localhost:7006/mcp",
                "transport": "streamable-http",
                "env": {"DANGEROUSLY_OMIT_AUTH": "true"}
            }
        }
    }
    ```

## MCP Tools

### query_sensor_status
Query the current status of a specific sensor.

**Parameters**:
- `entity_id` (string): The sensor entity ID (e.g., "home/livingroom_light/state")

**Returns**: Current sensor state and metadata

### query_sensor_record
Query historical sensor records with optional filters.

**Parameters**:
- `entity_ids` (list): List of sensor entity IDs
- `start_time` (string, optional): Start time in ISO format
- `end_time` (string, optional): End time in ISO format
- `limit` (number, optional): Maximum number of records to return

**Returns**: Historical sensor data

### query_sensor_group
Query multiple sensors status in SensorDB.

**Parameters**:
- `entity_ids` (list): List of sensor entity IDs

**Returns**: Current states of multiple sensors

## MQTT Topics

The service subscribes to the following topic patterns:
- `home/+/state` - Light states
- `home/+/temperature` - Temperature readings
- `home/+_motion/state` - Motion sensor states
- `home/+/state` - Door and window states
- `home/+_presence/state` - Presence sensor states

## Architecture

- **Background Thread**: MQTT subscription and information update processing
- **ServiceDB Integration**: Forwards updates via MQTT to ServiceDB
- **Local Cache**: Maintains current information states in memory
- **MCP Interface**: Provides query tools for external clients
- **Extensible Design**: Easy to add new module support 