import data

key="front_door_sensor"
data.config_topic[key] = 'homeassistant/binary_sensor/front_door/config'
data.state_topic[key] = "home/front_door/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Door",
  "state_topic": "home/front_door/state",
  "device_class": "door",
  "unique_id": "front_door_01",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["front_door_device"],
    "name": "Front",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""



key="back_door_sensor"
data.config_topic[key] = 'homeassistant/binary_sensor/Back_door/config'
data.state_topic[key] = "home/Back_door/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Door",
  "state_topic": "home/Back_door/state",
  "device_class": "door",
  "unique_id": "Back_door_01",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["Back_door_device"],
    "name": "Back",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""


key="garage_door_sensor"
data.config_topic[key] = 'homeassistant/binary_sensor/garage_door/config'
data.state_topic[key] = "home/garage_door/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Door",
  "state_topic": "home/garage_door/state",
  "device_class": "door",
  "unique_id": "garage_door_01",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["garage_door_device"],
    "name": "Garage",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""



