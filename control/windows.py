import data


key="kitchen window"
data.config_topic[key] = 'homeassistant/binary_sensor/window/config'
data.state_topic[key] =  'home/kitchen_window/state'
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Window",
  "state_topic": "home/kitchen_window/state",
  "device_class": "window",
  "unique_id": "window_01",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["window_device0"],
    "name": "Kitchen ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""


key="bathroom window"
data.config_topic[key] = 'homeassistant/binary_sensor/window1/config'
data.state_topic[key] =  "home/bathroom_window/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Window",
  "state_topic": "home/bathroom_window/state",
  "device_class": "window",
  "unique_id": "window_02",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["window_device1"],
    "name": "Bathroom ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""


key="bedroom 1 window"
data.config_topic[key] = 'homeassistant/binary_sensor/window2/config'
data.state_topic[key] =  "home/bedroom_1_window/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Window",
  "state_topic": "home/bedroom_1_window/state",
  "device_class": "window",
  "unique_id": "window_bedroom1",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["window_device2"],
    "name": "Bedroom 1 ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""



key="bedroom 2 window"
data.config_topic[key] = 'homeassistant/binary_sensor/window3/config'
data.state_topic[key] =  "home/bedroom_2_window/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Window",
  "state_topic": "home/bedroom_2_window/state",
  "device_class": "window",
  "unique_id": "window_bedroom2",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["window_device3"],
    "name": "Bedroom 2 ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""


key="living room window"
data.config_topic[key] = 'homeassistant/binary_sensor/window4/config'
data.state_topic[key] =  "home/livingroom_window/state"
data.default_state[key] = "CLOSED"
data.config_msg[key] = """{
  "name": "Window",
  "state_topic": "home/livingroom_window/state",
  "device_class": "window",
  "unique_id": "window_livingroom_1",
  "payload_on": "OPEN",
  "payload_off": "CLOSED",
  "device": {
    "identifiers": ["window_device4"],
    "name": "Living Room ",
    "manufacturer": "DIY",
    "model": "Magnetic Contact"
  }
}"""






