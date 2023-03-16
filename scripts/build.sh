#!/bin/bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py makemigrations --noinput
python manage.py migrate --noinput

python manage.py superuser || true

python manage.py collectstatic --noinput
