#!/bin/bash
export FLASK_APP=run.py
flask db init
flask db migrate
flask db upgrade
python3 run.py