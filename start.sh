#!/bin/bash

python3 /app/manage.py migrate
python3 /app/manage.py seed

python3 /app/manage.py runserver 0.0.0.0:8000
