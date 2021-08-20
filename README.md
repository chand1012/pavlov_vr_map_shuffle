# Pavlov Map Rotation Generator

- `maps.json` Only need the `id` and `title` of each map. 
    - `id` is the SteamID64 of the map. 
    - The example in this repo was generated with [pavlov-vr-rcon](https://github.com/Krzychu81/pavlov-vr-rcon).
- `lock.json` is the `id` matched with the [gamemode](http://wiki.pavlov-vr.com/index.php?title=Dedicated_server#Configuring_Game.ini) that the map requires. 
- After that is finished, run with `python shuffle.py`.
- Paste the output text (found in `rotation.txt`) at the bottom of your Pavlov server's `Game.ini` file.

More details on Pavlov server configuration can be found [here](http://wiki.pavlov-vr.com/index.php?title=Dedicated_server).