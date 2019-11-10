#!/usr/bin/env bash

echo "Look Makemigrations"
python manage.py makemigrations

echo "Start Migrate"
python manage.py migrate

echo "Start Project"
python manage.py runserver 0.0.0.0:8000