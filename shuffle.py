import json
import random
from string import Template

mapTemplateString = Template('MapRotation=(MapId="UGC$map", GameMode="$gm") # $name')

# game mode list
game_modes = ["GUN", "TDM", "DM"]

map_data = {}

# open map.json
with open("maps.json", "r") as map_file:
    map_data = json.load(map_file)

lock_data = {}

try: 
    with open("lock.json", "r") as lock_file:
        lock_data = json.load(lock_file)
except FileNotFoundError:
    pass

map_list = map_data.get('maps')

used_maps = []

rotation = []

mode = 0

rotation_length = 0

while rotation_length < len(map_list):
    m = random.choice(map_list)
    if m not in used_maps:
        if m['id'] in lock_data:
            used_maps.append(m)
            rotation.append(mapTemplateString.substitute(map=m['id'], gm=lock_data[m['id']], name=m['title']))
            rotation_length += 1
            continue
        used_maps.append(m)
        rotation.append(mapTemplateString.substitute(map=m['id'], gm=game_modes[mode], name=m['title']))
        mode += 1
        if mode == len(game_modes):
            mode = 0
        rotation_length += 1

with open('rotation.txt', 'w') as f:
    f.write('\n'.join(rotation))