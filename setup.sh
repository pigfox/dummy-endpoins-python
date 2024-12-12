#!/bin/bash
set -e
set -x

# Create virtual environments if not already created
python3 -m venv venv
python3 -m venv client/venv
python3 -m venv server/venv

# Activate main virtual environment
source venv/bin/activate

# Install global requirements
pip install requests flask

# Install requirements in specific virtual environments
source client/venv/bin/activate
pip install requests
deactivate

source server/venv/bin/activate
pip install flask
deactivate