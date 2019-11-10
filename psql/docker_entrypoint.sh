#!/usr/bin/env bash

echo "Look Makemigrations"
python mysite/manage.py makemigrations

echo "Start Migrate"
python mysite/manage.py migrate

echo "Start Project"
python mysite/manage.py runserver 0.0.0.0:8000