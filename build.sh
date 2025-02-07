#!/bin/bash

# Exit the script immediately if a command exits with a non-zero status
set -e

echo "Starting build process..."

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create a superuser if you want to ensure admin access (optional)
# echo "Creating superuser..."
# python manage.py createsuperuser --noinput --username admin --email admin@example.com

# If you're using `dj-database-url` or similar, set the environment variables here
# For example:
# export DATABASE_URL=$RENDER_DATABASE_URL

echo "Build process complete!"
python manage.py makemigrations
python manage.py migrate


