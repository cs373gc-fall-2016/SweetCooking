#!/bin/bash

clear

echo "Starting SweetCooking FLASK APP"
export FLASK_DEBUG=1
export FLASK_APP=run.py
flask run
