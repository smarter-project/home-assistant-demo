import data

key="kitchen motion"
data.config_topic[key]='homeassistant/binary_sensor/motion/config'
data.state_topic[key] = "home/kitchen_motion/state"
data.default_state[key] = "CLOSED"

data.config_msg[key] = """{
  "name": "Motion",
  "state_topic": "home/kitchen_motion/state",
  "device_class": "motion",
  "unique_id": "motion_01",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["motion_device"],
    "name": "Kitchen",
    "manufacturer": "DIY",
    "model": "Infrared2"
  }
}"""""



key="bathroom motion"
data.config_topic[key] = 'homeassistant/binary_sensor/motion1/config'
data.state_topic[key] = "home/bathroom_motion/state"
data.default_state[key] = "CLOSED"

data.config_msg[key] = """{
  "name": "Motion",
  "state_topic": "home/bathroom_motion/state",
  "device_class": "motion",
  "unique_id": "motion_02",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["motion_device1"],
    "name": "Bathroom ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""


key = "bedroom 1 motion"
data.config_topic[key] = 'homeassistant/binary_sensor/motion2/config'
data.state_topic[key] = "home/bedroom_1_motion/state"
data.default_state[key] = "CLOSED"

data.config_msg[key] = """{
  "name": "Motion",
  "state_topic": "home/bedroom_1_motion/state",
  "device_class": "motion",
  "unique_id": "motion_bedroom1",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["motion_device2"],
    "name": "Bedroom 1 ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""


key = "bedroom 2 motion"
data.config_topic[key] = 'homeassistant/binary_sensor/motion3/config'
data.state_topic[key] = "home/bedroom_2_motion/state"
data.default_state[key] = "CLOSED"

data.config_msg[key] = """{
  "name": "Motion",
  "state_topic": "home/bedroom_2_motion/state",
  "device_class": "motion",
  "unique_id": "motion_bedroom2",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["motion_device3"],
    "name": "Bedroom 2 ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""




key = "living room motion"
data.config_topic[key] = 'homeassistant/binary_sensor/motion4/config'
data.state_topic[key] = "home/livingroom_motion/state"
data.default_state[key] = "CLOSED"

data.config_msg[key] = """{
  "name": "Motion",
  "state_topic": "home/livingroom_motion/state",
  "device_class": "motion",
  "unique_id": "motion_livingroom",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["motion_device4"],
    "name": "Living Room ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""



key = "garden motion"
data.config_topic[key] = 'homeassistant/binary_sensor/motion5/config'
data.state_topic[key] = "home/garden_motion/state"
data.default_state[key] = "CLOSED"

data.config_msg[key] = """{
  "name": " Motion",
  "state_topic": "home/garden_motion/state",
  "device_class": "motion",
  "unique_id": "motion_garden",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["motion_device5"],
    "name": "Garden ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""


key = "garage motion"
data.config_topic[key] = 'homeassistant/binary_sensor/motion6/config'
data.state_topic[key] = "home/garage_motion/state"
data.default_state[key] = "CLOSED"

data.config_msg[key] = """{
  "name": "Motion",
  "state_topic": "home/garage_motion/state",
  "device_class": "motion",
  "unique_id": "motion_garage",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["motion_device6"],
    "name": "Garage ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""



key = "hallway motion"
data.config_topic[key] = 'homeassistant/binary_sensor/motion7/config'
data.state_topic[key] = "home/hallway_motion/state"
data.default_state[key] = "CLOSED"

data.config_msg[key] = """{
  "name": "Motion",
  "state_topic": "home/hallway_motion/state",
  "device_class": "motion",
  "unique_id": "motion_hallway",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["motion_device7"],
    "name": "Hallway ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""



