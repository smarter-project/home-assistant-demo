import data

key="living room light"
data.config_topic[key] = 'homeassistant/light/livingroom/config'
data.state_topic[key] =  'home/livingroom_light/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "Light",
  "command_topic": "home/livingroom_light/set",
  "state_topic": "home/livingroom_light/state",
  "unique_id": "livingroom_light_01",
  "payload_on": "ON",
  "payload_off": "OFF",
  "optimistic": "true",
  "device": {
    "identifiers": ["livingroom_light_device"],
    "name": "Living Room",
    "manufacturer": "DIY",
    "model": "MQTT Light v1"
  }
}"""


key="bedroom 1 light"
data.config_topic[key] ='homeassistant/light/bedroom1/config'
data.state_topic[key] = 'home/bedroom1_light/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "Light",
  "command_topic": "home/bedroom1_light/set",
  "state_topic": "home/bedroom1_light/state",
  "unique_id": "bedroom1_light_01",
  "payload_on": "ON",
  "payload_off": "OFF",
  "optimistic": "true",
  "device": {
    "identifiers": ["bedroom1_light_device"],
    "name": "Bedroom 1",
    "manufacturer": "DIY",
    "model": "MQTT Light v1"
  }
}"""


key="bedroom 2 light"
data.config_topic[key] ='homeassistant/light/bedroom2/config'
data.state_topic[key] = 'home/bedroom2_light/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "Light",
  "command_topic": "home/bedroom2_light/set",
  "state_topic": "home/bedroom2_light/state",
  "unique_id": "bedroom2_light_01",
  "payload_on": "ON",
  "payload_off": "OFF",
  "optimistic": "true",
  "device": {
    "identifiers": ["bedroom2_light_device"],
    "name": "Bedroom 2",
    "manufacturer": "DIY",
    "model": "MQTT Light v1"
  }
}"""



key="hallway light"
data.config_topic[key] ='homeassistant/light/hallway/config'
data.state_topic[key] = 'home/hallway_light/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "Light",
  "command_topic": "home/hallway_light/set",
  "state_topic": "home/hallway_light/state",
  "unique_id": "hallway_light_01",
  "payload_on": "ON",
  "payload_off": "OFF",
  "optimistic": "true",
  "device": {
    "identifiers": ["hallway_light_device"],
    "name": "Hallway",
    "manufacturer": "DIY",
    "model": "MQTT Light v1"
  }
}"""


key="kitchen light"
data.config_topic[key] ='homeassistant/light/kitchen/config'
data.state_topic[key] = 'home/kitchen_light/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "Light",
  "command_topic": "home/kitchen_light/set",
  "state_topic": "home/kitchen_light/state",
  "unique_id": "kitchen_light_01",
  "payload_on": "ON",
  "payload_off": "OFF",
  "optimistic": "true",
  "device": {
    "identifiers": ["kitchen_light_device"],
    "name": "Kitchen",
    "manufacturer": "DIY",
    "model": "MQTT Light v1"
  }
}"""





key="garage light"
data.config_topic[key] ='homeassistant/light/garage/config'
data.state_topic[key] = 'home/garage_light/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "Light",
  "command_topic": "home/garage_light/set",
  "state_topic": "home/garage_light/state",
  "unique_id": "garage_light_01",
  "payload_on": "ON",
  "payload_off": "OFF",
  "optimistic": "true",
  "device": {
    "identifiers": ["garage_light_device"],
    "name": "Garage",
    "manufacturer": "DIY",
    "model": "MQTT Light v1"
  }
}"""


key="bathroom_light"
data.config_topic[key] ='homeassistant/light/bathroom/config'
data.state_topic[key] = 'home/bathroom_light/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "Light",
  "command_topic": "home/bathroom_light/set",
  "state_topic": "home/bathroom_light/state",
  "unique_id": "bathroom_light_01",
  "payload_on": "ON",
  "payload_off": "OFF",
  "optimistic": "true",
  "device": {
    "identifiers": ["bathroom_light_device"],
    "name": "Bathroom",
    "manufacturer": "DIY",
    "model": "MQTT Light v1"
  }
}"""


key="garden_light"
data.config_topic[key] ='homeassistant/light/garden/config'
data.state_topic[key] = 'home/garden_light/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "Light",
  "command_topic": "home/garden_light/set",
  "state_topic": "home/garden_light/state",
  "unique_id": "garden_light_01",
  "payload_on": "ON",
  "payload_off": "OFF",
  "optimistic": "true",
  "device": {
    "identifiers": ["garden_light_device"],
    "name": "Garden",
    "manufacturer": "DIY",
    "model": "MQTT Light v1"
  }
}"""








