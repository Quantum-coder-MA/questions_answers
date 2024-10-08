#!/bin/sh

# Activate virtual environment if you have one (optional)
# source /path/to/your/venv/bin/activate

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the server
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
