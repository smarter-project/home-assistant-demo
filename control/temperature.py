import data

key="livingroom_temperature"
data.config_topic[key] = 'homeassistant/sensor/livingroom_temperature/config'
data.state_topic[key] = "home/living_room/temperature"
data.default_state[key] = "19.8"
data.config_msg[key] = """{
  "name": "Temperature",
  "state_topic": "home/living_room/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "value_template": "{{ value | float }}",
  "unique_id": "living_room_temperature_01",
  "optimistic": "true",
  "device": {
    "identifiers": ["living_room_sensor_01"],
    "name": "Living Room ",
    "manufacturer": "DIY",
    "model": "ESP32 TempSensor"
  }
}"""




key="bedroom 1 temperature"
data.config_topic[key] = 'homeassistant/sensor/bedroom1_temperature/config'
data.state_topic[key] = "home/bedroom1/temperature"
data.default_state[key] = "19.8"
data.config_msg[key] = """{
  "name": "Temperature",
  "state_topic": "home/bedroom1/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "value_template": "{{ value | float }}",
  "unique_id": "bedroom1_temperature_01",
  "device": {
    "identifiers": ["bedroom1_sensor_01"],
    "name": "Bedroom 1 ",
    "manufacturer": "DIY",
    "model": "ESP32 TempSensor"
  }
}"""




key="bedroom 2 temperature"
data.config_topic[key] = 'homeassistant/sensor/bedroom2_temperature/config'
data.state_topic[key] = "home/bedroom2/temperature"
data.default_state[key] = "19.8"
data.config_msg[key] = """{
  "name": "Temperature",
  "state_topic": "home/bedroom2/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "value_template": "{{ value | float }}",
  "unique_id": "bedroom2_temperature_01",
  "device": {
    "identifiers": ["bedroom2_sensor_01"],
    "name": "Bedroom 2 ",
    "manufacturer": "DIY",
    "model": "ESP32 TempSensor"
  }
}"""




key="kitchen temperature"
data.config_topic[key] = 'homeassistant/sensor/kitchen_temperature/config'
data.state_topic[key] = "home/kitchen/temperature"
data.default_state[key] = "19.8"
data.config_msg[key] = """{
  "name": "Temperature",
  "state_topic": "home/kitchen/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "value_template": "{{ value | float }}",
  "unique_id": "kitchen_temperature_01",
  "device": {
    "identifiers": ["kitchen_sensor_01"],
    "name": "Kitchen ",
    "manufacturer": "DIY",
    "model": "ESP32 TempSensor"
  }
}"""





key="hallway temperature"
data.config_topic[key] = 'homeassistant/sensor/hallway_temperature/config'
data.state_topic[key] = "home/hallway/temperature"
data.default_state[key] = "19.8"
data.config_msg[key] = """{
  "name": "Temperature",
  "state_topic": "home/hallway/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "value_template": "{{ value | float }}",
  "unique_id": "hallway_temperature_01",
  "device": {
    "identifiers": ["hallway_sensor_01"],
    "name": "Hallway ",
    "manufacturer": "DIY",
    "model": "ESP32 TempSensor"
  }
}"""




key="garage temperature"
data.config_topic[key] = 'homeassistant/sensor/garage_temperature/config'
data.state_topic[key] = "home/garage/temperature"
data.default_state[key] = "19.8"
data.config_msg[key] = """{
  "name": "Temperature",
  "state_topic": "home/garage/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "value_template": "{{ value | float }}",
  "unique_id": "garage_temperature_01",
  "device": {
    "identifiers": ["garage_sensor_01"],
    "name": "Garage ",
    "manufacturer": "DIY",
    "model": "ESP32 TempSensor"
  }
}"""


key="bathroom temperature"
data.config_topic[key] = 'homeassistant/sensor/bathroom_temperature/config'
data.state_topic[key] = "home/bathroom/temperature"
data.default_state[key] = "19.8"
data.config_msg[key] = """{
  "name": "Temperature",
  "state_topic": "home/bathroom/temperature",
  "unit_of_measurement": "°C",
  "device_class": "temperature",
  "value_template": "{{ value | float }}",
  "unique_id": "bathroom_temperature_01",
  "device": {
    "identifiers": ["bathroom_sensor_01"],
    "name": "Bathroom ",
    "manufacturer": "DIY",
    "model": "ESP32 TempSensor"
  }
}"""


