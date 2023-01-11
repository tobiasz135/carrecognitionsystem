#!/bin/sh
screen -d -m "node /services/socketServer/index.js"
npm i
screen -d -m "npm run dev"
python3 run_app.py