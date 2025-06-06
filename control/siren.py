import data

key="siren"
data.config_topic[key] = 'homeassistant/siren/hallway/config'
data.state_topic[key] =  'home/hallway/siren/state'
data.default_state[key] = "OFF"
data.config_msg[key] = """{
  "name": "siren",
  "command_topic": "home/hallway/siren/set",
  "state_topic": "home/hallway/siren/state",
  "payload_on" : "ON",
  "payload_off": "OFF",
  "unique_id": "siren_01",
  "optimistic": "true",
  "device": {
    "identifiers": ["siren_device"],
    "name": "hallway",
    "manufacturer": "DIY",
    "model": "MQTT siren"
  }
}"""

