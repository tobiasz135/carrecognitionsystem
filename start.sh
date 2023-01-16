#!/bin/sh
# This script is used to start the server
screen -d -m "node /services/socketServer/index.js"
screen -d -m "npm run dev"
python3 run_app.py