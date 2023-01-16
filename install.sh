#!/bin/sh
apt install npm
apt install libgtk2.0-dev
pip install -r requirements.txt
apt install screen
apt install tesseract-ocr -y
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

npm install express
npm i
npm install next react react-dom