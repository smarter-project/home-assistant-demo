# server.py
# -*- coding: utf-8 -*-
"""
Information Retrieval MCP Server for Home Assistant

• Subscribes to various MQTT topics from Home Assistant modules
• Captures information updates and forwards to ServiceDB
• Provides MCP tools for querying information status and records
"""

import json
import logging
from math import log
import os
import sys
import threading
import time
import uuid
from collections.abc import AsyncIterator
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Optional, List

import paho.mqtt.client as mqtt
from mcp.server.fastmcp import FastMCP
from contextlib import asynccontextmanager

# Path to initial sensor status JSON
INITIAL_SENSOR_STATUS_PATH = os.getenv("INITIAL_SENSOR_STATUS_PATH", os.path.join(os.path.dirname(__file__), "../../initial_sensor_status.json"))

# Configure logger
logger = logging.getLogger("info_retrieval_mcp")
logger.setLevel(logging.DEBUG)
if not logger.handlers:
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(console_handler)


# ────────────────────────────────
# Configuration
# ────────────────────────────────
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))

# Sensor topics to subscribe to (based on control folder analysis)
SENSOR_TOPICS = [
    # # Lights
    # "home/+/light/state",
    # Temperature
    # "home/+/temperature",
    # # Motion
    # "home/+/motion/state",
    # # Doors
    # "home/+/door/state",
    # # Windows
    # "home/+/window/state",
    # # Presence
    # "home/+/presence/state",
    # # Siren
    # "home/+/siren/state",
    # # Cameras
    # "home/+/camera",
    # # Alarm
    # "home/alarm",
    "home/#",
]


# ────────────────────────────────
# ServiceDB Client for MQTT Communication
# ────────────────────────────────
class ServiceDBClient:
    def __init__(self, mqtt_broker: str = "localhost", mqtt_port: int = 1883):
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.client = mqtt.Client()
        self.request_responses: Dict[str, Dict[str, Any]] = {}  # request_id -> response data
        self.request_events: Dict[str, threading.Event] = {}    # request_id -> event for waiting
        
        # Setup MQTT callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
    
    def on_connect(self, client, userdata, flags, rc):
        """MQTT connection callback"""
        if rc == 0:
            logger.info(f"Connected to MQTT broker at {self.mqtt_broker}:{self.mqtt_port}")
            # Subscribe to ServiceDB response topic
            self.client.subscribe("modules_DB/ServiceDB/response/#")
        else:
            logger.error(f"Failed to connect to MQTT broker, return code: {rc}")
    
    def on_disconnect(self, client, userdata, rc):
        """MQTT disconnection callback"""
        if rc != 0:
            logger.warning(f"Unexpected disconnection from MQTT broker, return code: {rc}")
    
    def on_message(self, client, userdata, msg):
        """MQTT message callback"""
        try:
            response = json.loads(msg.payload.decode())
            request_id = response.get("response_to")
            
            if request_id and request_id in self.request_responses:
                # Store response and signal waiting thread
                self.request_responses[request_id] = response
                if request_id in self.request_events:
                    self.request_events[request_id].set()
                logger.debug(f"Response received for request {request_id}: {response}")
            else:
                logger.debug(f"Response received for unknown request {request_id}")
                
        except Exception as e:
            logger.error(f"Error processing response: {e}")
    
    def connect(self):
        """Connect to MQTT broker"""
        try:
            self.client.connect(self.mqtt_broker, self.mqtt_port, 60)
            self.client.loop_start()
            time.sleep(1)  # Wait for connection
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from MQTT broker"""
        self.client.loop_stop()
        self.client.disconnect()
    
    def send_request(self, request_type: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Send request to ServiceDB and wait for response"""
        request_id = str(uuid.uuid4())
        
        # Create event for this request
        event = threading.Event()
        self.request_events[request_id] = event
        self.request_responses[request_id] = {}
        
        request = {
            "request_id": request_id,
            "type": request_type,
            "payload": data
        }
        
        logger.debug(f"Sending request: {request_type}")
        logger.debug(f"Request ID: {request_id}")
        
        try:
            self.client.publish("modules_DB/ServiceDB/request", json.dumps(request))
            
            # Wait for response (timeout: 60 seconds)
            if event.wait(timeout=60):
                response = self.request_responses.get(request_id)
                # Clean up
                if request_id in self.request_responses:
                    del self.request_responses[request_id]
                if request_id in self.request_events:
                    del self.request_events[request_id]
                return response
            else:
                logger.error(f"Request {request_id} timed out")
                # Clean up
                if request_id in self.request_responses:
                    del self.request_responses[request_id]
                if request_id in self.request_events:
                    del self.request_events[request_id]
                return None
            
        except Exception as e:
            logger.error(f"Error sending request: {e}")
            # Clean up
            if request_id in self.request_responses:
                del self.request_responses[request_id]
            if request_id in self.request_events:
                del self.request_events[request_id]
            return None


# ────────────────────────────────
# Sensor Manager for MQTT Subscription
# ────────────────────────────────
class SensorManager:
    def __init__(self, servicedb_client: ServiceDBClient):
        self.servicedb_client = servicedb_client
        self.mqtt_client = mqtt.Client()
        self.sensor_map: Dict[str, Dict[str, Any]] = self._load_initial_sensor_map()
        self.running = False
        
        # Setup MQTT callbacks
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.on_disconnect = self.on_disconnect
    
    def _load_initial_sensor_map(self) -> Dict[str, Dict[str, Any]]:
        try:
            with open(INITIAL_SENSOR_STATUS_PATH, "r") as f:
                sensors = json.load(f)
            sensor_map = {sensor["entity_id"]: sensor for sensor in sensors}
            logger.info(f"Loaded {len(sensor_map)} sensors from initial_sensor_status.json")
            return sensor_map
        except Exception as e:
            logger.error(f"Failed to load initial_sensor_status.json: {e}")
            return {}

    def on_connect(self, client, userdata, flags, rc):
        """MQTT connection callback"""
        if rc == 0:
            logger.info("Sensor Manager connected to MQTT broker")
            # Subscribe to all sensor topics
            for topic in SENSOR_TOPICS:
                self.mqtt_client.subscribe(topic)
                logger.info(f"Subscribed to sensor topic: {topic}")
        else:
            logger.error(f"Failed to connect to MQTT broker, return code: {rc}")
    
    def on_disconnect(self, client, userdata, rc):
        """MQTT disconnection callback"""
        if rc != 0:
            logger.warning(f"Unexpected disconnection from MQTT broker, return code: {rc}")
    
    def on_message(self, client, userdata, msg):
        """MQTT message callback for sensor updates"""
        try:
            topic = msg.topic
            timestamp = datetime.now().isoformat()

            # Try to decode payload as UTF-8, fallback to base64 for binary data
            try:
                payload = msg.payload.decode('utf-8')
                logger.debug(f"Received sensor update: {topic} = {payload}")
            except UnicodeDecodeError:
                # If UTF-8 decode fails, it might be binary data
                import base64
                payload = base64.b64encode(msg.payload).decode('utf-8')
                logger.debug(f"Received binary sensor update: {topic} = [base64 encoded]")
                # TBD in the future. 
                return

            # Only update if topic is in sensor_map
            if topic not in self.sensor_map:
                logger.error(f"MQTT topic {topic} not found in sensor_map. Skipping update.")
                return

            # Update only the state field, keep all other fields in map
            self.sensor_map[topic]["state"] = payload
            self.sensor_map[topic]["last_changed"] = timestamp
            self.sensor_map[topic]["last_updated"] = timestamp

            # Prepare minimal update for ServiceDB
            update_msg = {
                "entity_id": topic,
                "state": payload, 
                "last_changed": timestamp,
                "last_updated": timestamp
            }
            # logger.debug(f"Forwarding minimal update to ServiceDB: {update_msg}")
            self._forward_to_servicedb(update_msg)

        except Exception as e:
            logger.error(f"Error processing sensor message: {e}")
            logger.error(f"[MQTT] Received message on topic: {msg.topic}")
            logger.error(f"[MQTT] Received message payload type: {type(msg.payload)}, length: {len(msg.payload)}")
            if len(msg.payload) <= 100:  # Only log small payloads to avoid spam
                logger.error(f"[MQTT] Received message payload: {msg.payload}")
    
    def _get_device_class(self, topic: str) -> str:
        """Extract device class from topic"""
        if "light" in topic:
            return "light"
        elif "temperature" in topic:
            return "temperature"
        elif "motion" in topic:
            return "motion"
        elif "door" in topic:
            return "door"
        elif "window" in topic:
            return "window"
        elif "presence" in topic:
            return "presence"
        elif "siren" in topic:
            return "siren"
        elif "alarm" in topic:
            return "alarm"
        elif "camera" in topic:
            return "camera"
        else:
            return "unknown"
    
    def _get_friendly_name(self, topic: str) -> str:
        """Extract friendly name from topic"""
        parts = topic.split('/')
        if len(parts) >= 2:
            room = parts[1].replace('_', ' ').title()
            sensor_type = self._get_device_class(topic).title()
            return f"{room} {sensor_type}"
        return topic
    
    def _get_room(self, topic: str) -> str:
        """Extract room from topic"""
        parts = topic.split('/')
        if len(parts) >= 2:
            return parts[1].replace('_', ' ')
        return "unknown"
    
    def _get_sensor_type(self, topic: str) -> str:
        """Extract sensor type from topic"""
        return self._get_device_class(topic)
    
    def _forward_to_servicedb(self, sensor_data: Dict[str, Any]):
        """Forward sensor update to ServiceDB"""
        try:
            response = self.servicedb_client.send_request("sensordb_update_sensor", sensor_data)
            if response and response.get("status") == "ok":
                result = response.get("result", {})
                if result.get("success", False):
                    logger.debug(f"Successfully forwarded sensor update to ServiceDB: {sensor_data['entity_id']}")
                    # logger.debug(f"Updated fields: {result.get('updated_fields', [])}")
                else:
                    logger.warning(f"ServiceDB update returned success=false for: {sensor_data['entity_id']}")
            else:
                error_msg = response.get("error", "Unknown error") if response else "No response"
                logger.error(f"Failed to forward sensor update to ServiceDB: {sensor_data['entity_id']}, Error: {error_msg}")
        except Exception as e:
            logger.error(f"Error forwarding to ServiceDB: {e}")
    
    def connect(self, broker: str, port: int) -> bool:
        """Connect to MQTT broker"""
        try:
            self.mqtt_client.connect(broker, port, 60)
            self.mqtt_client.loop_start()
            time.sleep(1)  # Wait for connection
            self.running = True
            return True
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from MQTT broker"""
        self.running = False
        self.mqtt_client.loop_stop()
        self.mqtt_client.disconnect()
    
    def get_sensor_status(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """Get current sensor status from map"""
        return self.sensor_map.get(entity_id)
    
    def get_all_sensors(self) -> Dict[str, Dict[str, Any]]:
        """Get all sensor statuses from map"""
        return self.sensor_map.copy()


# ────────────────────────────────
# Context dataclass stored for every request
# ────────────────────────────────
@dataclass
class AppContext:
    servicedb_client: ServiceDBClient
    sensor_manager: SensorManager


# ────────────────────────────────
# Lifespan: connect to ServiceDB & start sensor monitoring
# ────────────────────────────────
async def _connect_servicedb() -> ServiceDBClient:
    """Connect to ServiceDB via MQTT."""
    logger.info(f"Attempting to connect to ServiceDB at {MQTT_BROKER}:{MQTT_PORT}")
    client = ServiceDBClient(MQTT_BROKER, MQTT_PORT)
    if not client.connect():
        logger.error(f"Failed to connect to ServiceDB at {MQTT_BROKER}:{MQTT_PORT}")
        raise RuntimeError(f"Failed to connect to ServiceDB at {MQTT_BROKER}:{MQTT_PORT}")
    logger.info("Successfully connected to ServiceDB")
    return client


def _start_sensor_manager(servicedb_client: ServiceDBClient) -> SensorManager:
    """Start sensor manager in background thread."""
    logger.info("Starting sensor manager...")
    sensor_manager = SensorManager(servicedb_client)
    
    if not sensor_manager.connect(MQTT_BROKER, MQTT_PORT):
        raise RuntimeError(f"Failed to connect sensor manager to MQTT broker")
    
    logger.info("Sensor manager started successfully")
    return sensor_manager


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    logger.info("Starting app lifespan...")
    try:
        servicedb_client = await _connect_servicedb()
        logger.info("ServiceDB client connected successfully")
        
        sensor_manager = _start_sensor_manager(servicedb_client)
        logger.info("Sensor manager initialized successfully")
        
        logger.info("App lifespan initialization complete")
        yield AppContext(servicedb_client=servicedb_client, sensor_manager=sensor_manager)
        
    except Exception as e:
        logger.error(f"Failed to initialize app lifespan: {e}")
        raise
    finally:
        # Cleanup: disconnect from ServiceDB and stop sensor manager
        logger.info("Starting app lifespan cleanup...")
        try:
            if 'sensor_manager' in locals():
                sensor_manager.disconnect()
                logger.info("Sensor manager disconnected")
        except Exception as e:
            logger.error(f"Error disconnecting sensor manager: {e}")
        
        try:
            if 'servicedb_client' in locals():
                servicedb_client.disconnect()
                logger.info("ServiceDB client disconnected")
        except Exception as e:
            logger.error(f"Error disconnecting ServiceDB client: {e}")
        
        logger.info("App lifespan cleanup complete.")


# ────────────────────────────────
# FastMCP app
# ────────────────────────────────
mcp = FastMCP(
    "Information Retrieval Service",
    version="1.0.0",
    dependencies=["paho-mqtt"],
    lifespan=app_lifespan,
)


# ────────────────────────────────
# MCP Tools
# ────────────────────────────────
@mcp.tool()
def query_sensor_status(entity_id: str) -> str:
    """
    Query the current status of a specific sensor.

    Args
    ----
    entity_id : str
        The sensor entity ID (e.g., "home/livingroom_light/state")

    Returns
    -------
    str
        JSON string containing current sensor state and metadata
    """
    logger.info(f"query_sensor_status tool invoked for entity_id: {entity_id}")
    
    app_ctx: AppContext = mcp.get_context().request_context.lifespan_context
    
    # First check local cache
    sensor_data = app_ctx.sensor_manager.get_sensor_status(entity_id)
    
    if sensor_data:
        return json.dumps(sensor_data, indent=2)
    
    # If not in cache, query ServiceDB
    try:
        response = app_ctx.servicedb_client.send_request("sensordb_query_sensor", {
            "entity_id": entity_id
        })
        
        if response and response.get("status") == "ok":
            result = response.get("result", {})
            if result.get("success", False):
                sensor_info = result.get("sensor", {})
                return json.dumps(sensor_info, indent=2)
            else:
                return json.dumps({
                    "error": "Sensor not found in database",
                    "entity_id": entity_id
                }, indent=2)
        else:
            error_msg = response.get("error", "Unknown error") if response else "No response"
            return json.dumps({
                "error": error_msg,
                "entity_id": entity_id
            }, indent=2)
            
    except Exception as e:
        logger.error(f"Error querying sensor status: {e}")
        return json.dumps({
            "error": f"Failed to query sensor: {str(e)}",
            "entity_id": entity_id
        }, indent=2)


@mcp.tool()
def query_sensor_record(entity_ids: List[str], start_time: Optional[str] = None, 
                       end_time: Optional[str] = None, limit: Optional[str] = "100") -> str:
    """
    Query historical sensor records with optional filters.

    Args
    ----
    entity_ids : List[str]
        List of sensor entity IDs
    start_time : Optional[str]
        Start time in ISO format (e.g., "2025-01-01T00:00:00Z")
    end_time : Optional[str]
        End time in ISO format (e.g., "2025-01-31T23:59:59Z")
    limit : Optional[str]
        Maximum number of records to return (default: "100")

    Returns
    -------
    str
        JSON string containing historical sensor data
    """
    logger.info(f"query_sensor_record tool invoked for entity_ids: {entity_ids}")
    logger.debug(f"Raw parameters - start_time: '{start_time}', end_time: '{end_time}', limit: '{limit}'")
    
    app_ctx: AppContext = mcp.get_context().request_context.lifespan_context
    
    try:
        # Build query payload
        # if limit is not none, convert to int
        if limit:
            # if limit is convertable to int, convert to int
            try:
                rlimit = int(limit)
            except ValueError:
                rlimit = 100
        else:
            rlimit = 100
        
        # check start/end time, if not in ISO format, return error
        def is_valid_iso_format(time_str: str) -> bool:
            """Check if string is in valid ISO 8601 format"""
            if not time_str or len(time_str) < 19:  # Minimum length for ISO format
                return False
            try:
                # Try to parse as ISO format
                datetime.fromisoformat(time_str.replace('Z', '+00:00'))
                return True
            except ValueError:
                return False
        
        if start_time and not is_valid_iso_format(start_time):
            return json.dumps({
                "error": f"Invalid start_time format: '{start_time}'. Expected ISO format (YYYY-MM-DDTHH:MM:SSZ)",
                "entity_ids": entity_ids
            }, indent=2)
        if end_time and not is_valid_iso_format(end_time):
            return json.dumps({
                "error": f"Invalid end_time format: '{end_time}'. Expected ISO format (YYYY-MM-DDTHH:MM:SSZ)",
                "entity_ids": entity_ids
            }, indent=2)
        
        payload = {
            "entity_ids": entity_ids,
            "limit": rlimit
        }
        
        if start_time:
            payload["start_time"] = start_time
        if end_time:
            payload["end_time"] = end_time
        
        query_payload = {
            "op": "list",
            **payload
        }
        logger.debug(f"Querying ServiceDB with payload: {query_payload}")

        # Query ServiceDB
        response = app_ctx.servicedb_client.send_request("sensordb_query_OpFilter", query_payload)
        
        if response and response.get("status") == "ok":
            result = response.get("result", {})
            if result.get("success", False):
                return json.dumps(result, indent=2)
            else:
                return json.dumps({
                    "error": "Failed to query sensor records",
                    "entity_ids": entity_ids
                }, indent=2)
        else:
            error_msg = response.get("error", "Unknown error") if response else "No response"
            return json.dumps({
                "error": error_msg,
                "entity_ids": entity_ids
            }, indent=2)
            
    except Exception as e:
        logger.error(f"Error querying sensor records: {e}")
        return json.dumps({
            "error": f"Failed to query sensor records: {str(e)}",
            "entity_ids": entity_ids
        }, indent=2)


@mcp.tool()
def query_sensor_group(entity_ids: List[str]) -> str:
    """
    Query multiple sensors status in SensorDB.

    Args
    ----
    entity_ids : List[str]
        List of sensor entity IDs

    Returns
    -------
    str
        JSON string containing current states of multiple sensors
    """
    logger.info(f"query_sensor_group tool invoked for entity_ids: {entity_ids}")
    
    app_ctx: AppContext = mcp.get_context().request_context.lifespan_context

    # First check local cache
    sensor_data_list = []
    missing_sensors = []

    for entity_id in entity_ids:
        sensor_data = app_ctx.sensor_manager.get_sensor_status(entity_id)
        if sensor_data:
            sensor_data_list.append(sensor_data)
        else:
            missing_sensors.append(entity_id)

    if not missing_sensors:  # All found in cache
        logger.debug(f"All {len(entity_ids)} sensors found in cache")
        return json.dumps(sensor_data_list, indent=2)

    logger.debug(f"Cache miss for sensors: {missing_sensors}, querying ServiceDB")

    # If not in cache, query ServiceDB
    try:
        response = app_ctx.servicedb_client.send_request("sensordb_query_sensor_group", {
            "entity_ids": entity_ids
        })
        
        if response and response.get("status") == "ok":
            result = response.get("result", {})
            if result.get("success", False):
                return json.dumps(result, indent=2)
            else:
                return json.dumps({
                    "error": "Failed to query sensor group",
                    "entity_ids": entity_ids
                }, indent=2)
        else:
            error_msg = response.get("error", "Unknown error") if response else "No response"
            return json.dumps({
                "error": error_msg,
                "entity_ids": entity_ids
            }, indent=2)
            
    except Exception as e:
        logger.error(f"Error querying sensor group: {e}")
        return json.dumps({
            "error": f"Failed to query sensor group: {str(e)}",
            "entity_ids": entity_ids
        }, indent=2)


@mcp.tool()
def list_all_sensors() -> str:
    """
    List all available sensor entity_ids in the system.

    Returns
    -------
    str
        JSON string containing a list of all sensor entity_ids
    """
    logger.info("list_all_sensors tool invoked")
    app_ctx: AppContext = mcp.get_context().request_context.lifespan_context
    sensor_ids = list(app_ctx.sensor_manager.sensor_map.keys())
    return json.dumps({"sensor_entity_ids": sensor_ids}, indent=2)


if __name__ == "__main__":
    # Run the FastMCP server directly for local testing
    mcp.run() 