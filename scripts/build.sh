#!/bin/bash

set -o errexit  # exit on error

echo "Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed successfully :)"

echo "Running migrations..."
python manage.py migrate --noinput
echo "Migrations completed successfully :)"

echo "Creating superuser if it doesn't exist..."
python manage.py superuser || true
echo "Superuser created successfully :)"

echo "Collecting static files for production..."
python manage.py collectstatic --noinput
echo "Static files collected successfully :)"
