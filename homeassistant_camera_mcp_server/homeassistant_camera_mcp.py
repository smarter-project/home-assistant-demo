import os
import requests
import base64
from fastmcp import FastMCP

API_URL = "http://homeassistant:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0OTA4YzBjZmRlMTg0ZjAyOTE4Zjg4ODdjMzBiNGI4OCIsImlhdCI6MTc0ODUyNzQ4MCwiZXhwIjoyMDYzODg3NDgwfQ.MmXRZ38vUlKNijfYaBEdR_A2MoX7NwY_88lBe1BddfA"


def get_camera_snapshot(api_url: str, token: str, camera_id: str, save_path: str):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    url = f"{api_url}/api/camera_proxy/{camera_id}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        jpeg_bytes = response.content
        #encoded = base64.b64encode(jpeg_bytes).decode("utf-8")
        #return base64.b64encode(jpeg_bytes).decode("utf-8")
        with open(save_path, 'wb') as f:
            f.write(jpeg_bytes)
        print(f"Saved to {save_path}")
        return save_path
    except requests.RequestException as e:
        print(f"Error fetching snapshot: {e}")
        return ""
    
def get_camera_entities(api_url: str, token: str):
    """
    Return a list of camera entities from Home Assistant.

    Args:
        api_url: The base URL of your Home Assistant instance (e.g., http://localhost:8123).
        token: A long-lived access token from Home Assistant.

    Returns:
        A list of dictionaries containing camera entity data.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    try:
        response = requests.get(f"{api_url}/api/states", headers=headers)
        response.raise_for_status()
        entities = response.json()
        cameras = [
            entity for entity in entities if entity["entity_id"].startswith("camera.")
        ]
        return cameras
    except requests.RequestException as e:
        print(f"Error accessing Home Assistant API: {e}")
        return []
    

    
mcp = FastMCP("HomeAssistant Camera Server")

@mcp.tool()
def capture(name: str) -> str:
    """save a snapshot from the specified camera"""
    id = map_name_to_entity(name)
    snapshot_path = f"/images/{id}.jpg"
    if id != "":
        return get_camera_snapshot(
            api_url=API_URL,
            token=TOKEN,
            camera_id=id,
            save_path=snapshot_path
        )
    return "not ok"


@mcp.tool()
def get_cameras():
    """return a list of available cameras"""
    cameras = get_camera_entities(API_URL, TOKEN)
    cams = []
    for cam in cameras:
        cams.append(cam["attributes"].get("friendly_name", "Unnamed"))
    return cams


def map_name_to_entity(name: str):
    """return the entity id for a camera"""
    cameras = get_camera_entities(API_URL, TOKEN)
    cams = []
    for cam in cameras:
        if cam["attributes"].get("friendly_name", "Unnamed")==name:
            return cam["entity_id"]
    return []


# Define a dynamic resource that returns a greeting
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Return a personalized greeting."""
    return f"Hello, {name}!"

if __name__ == "__main__":
  mcp.run(transport="streamable_http",  host="0.0.0.0", port=9000)

    

