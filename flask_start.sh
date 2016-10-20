#!/bin/bash
clear

echo "Starting SweetCooking FLASK APP"
export FLASK_DEBUG=1
export SETTINGS=/home/rafik/Desktop/scooking/SweetCooking/app/envvar.py
export FLASK_APP=run.py
flask run
