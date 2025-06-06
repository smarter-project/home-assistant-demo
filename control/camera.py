import data

key="living room camera 1"
data.config_topic[key] = 'homeassistant/light/livingroom/config'
data.state_topic[key] =  'home/livingroom/camera1'
data.default_state[key] = "File: media/new_room1.png"

key="living room camera 2"
data.config_topic[key] = 'homeassistant/light/livingroom/config'
data.state_topic[key] =  'home/livingroom/camera2'
data.default_state[key] = "File: media/new_room.png"


key="Front door camera"
data.config_topic[key] = 'homeassistant/light/livingroom/config'
data.state_topic[key] =  'home/hallway/front_door_camera'
data.default_state[key] = "File: media/front.png"


