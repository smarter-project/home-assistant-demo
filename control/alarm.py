import data

key="alarm"
data.config_topic[key] = 'homeassistant/alarm/config'
data.state_topic[key] =  'home/alarm'
data.default_state[key] = "disarmed"
data.config_msg[key] = """{
  "name": "alarm",
  "command_topic": "home/alarm/set",
  "state_topic": "home/alarm",
  "code": "1234",
  "code_arm_required": "false",
  "unique_id": "alarm_01",
  "optimistic": "true",
  "device": {
    "identifiers": ["alarm_device"],
    "name": "alarm",
    "manufacturer": "DIY",
    "model": "MQTT alarm"
  }
}"""

