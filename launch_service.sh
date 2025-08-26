#!/bin/bash
cd /home/pi/pi-camera-stream-flask
git pull
source venv/bin/activate
python3 main.py
