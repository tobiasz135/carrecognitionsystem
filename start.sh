#!/bin/sh
# This script is used to start the server
screen -S node -dm
screen -S node -X exec node ./services/socketServer/index.js
screen -S website -dm
screen -S website -X nvm install v18.12.1
screen -S website -X exec npm run dev
#sleep 10
python3 run_app.py