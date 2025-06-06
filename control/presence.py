import data

key="kitchen presence"
data.config_topic[key]='homeassistant/binary_sensor/presence/config'
data.state_topic[key] = "home/kitchen_presence/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Presence",
  "state_topic": "home/kitchen_presence/state",
  "device_class": "presence",
  "unique_id": "presence_01",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["presence_device"],
    "name": "Kitchen",
    "suggested_area": "Kitchen",
    "manufacturer": "DIY",
    "model": "Infrared2"
  }
}"""""



key="bathroom presence"
data.config_topic[key] = 'homeassistant/binary_sensor/presence1/config'
data.state_topic[key] = "home/bathroom_presence/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Presence",
  "state_topic": "home/bathroom_presence/state",
  "device_class": "presence",
  "unique_id": "presence_02",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["presence_device1"],
    "name": "Bathroom ",
    "suggested_area": "Bathroom ",
    "manufacturer": "DIY",
    "model": "Multiway"
  }
}"""


key = "bedroom 1 presence"
data.config_topic[key] = 'homeassistant/binary_sensor/presence2/config'
data.state_topic[key] = "home/bedroom_1_presence/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Presence",
  "state_topic": "home/bedroom_1_presence/state",
  "device_class": "presence",
  "unique_id": "presence_bedroom1",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["presence_device2"],
    "name": "Bedroom 1 ",
    "suggested_area": "Bedroom 1 ",
    "manufacturer": "DIY",
    "model": "Multiway"
  }
}"""


key = "bedroom 2 presence"
data.config_topic[key] = 'homeassistant/binary_sensor/presence3/config'
data.state_topic[key] = "home/bedroom_2_presence/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Presence",
  "state_topic": "home/bedroom_2_presence/state",
  "device_class": "presence",
  "unique_id": "presence_bedroom2",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["presence_device3"],
    "name": "Bedroom 2 ",
    "suggested_area": "Bedroom 2 ",
    "manufacturer": "DIY",
    "model": "Multiway"
  }
}"""




key = "living room presence"
data.config_topic[key] = 'homeassistant/binary_sensor/presence4/config'
data.state_topic[key] = "home/livingroom_presence/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Presence",
  "state_topic": "home/livingroom_presence/state",
  "device_class": "presence",
  "unique_id": "presence_livingroom",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["presence_device4"],
    "name": "Living Room ",
    "suggested_area": "Living Room ",
    "manufacturer": "DIY",
    "model": "Multiway"
  }
}"""



key = "garden presence"
data.config_topic[key] = 'homeassistant/binary_sensor/presence5/config'
data.state_topic[key] = "home/garden_presence/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": " Presence",
  "state_topic": "home/garden_presence/state",
  "device_class": "presence",
  "unique_id": "presence_garden",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["presence_device5"],
    "name": "Garden ",
    "suggested_area": "Garden ",
    "manufacturer": "DIY",
    "model": "Multiway"
  }
}"""


key = "garage presence"
data.config_topic[key] = 'homeassistant/binary_sensor/presence6/config'
data.state_topic[key] = "home/garage_presence/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Presence",
  "state_topic": "home/garage_presence/state",
  "device_class": "presence",
  "unique_id": "presence_garage",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["presence_device6"],
    "name": "Garage ",
    "suggested_area": "garage ",
    "manufacturer": "DIY",
    "model": "Multiway"
  }
}"""



