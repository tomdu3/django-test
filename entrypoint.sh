#!/bin/sh

echo 'Running migrations...'
python manage.py migrate
echo 'Migrations complete.'

echo 'Running server...'
python manage.py runserver 0.0.0.0:8000
