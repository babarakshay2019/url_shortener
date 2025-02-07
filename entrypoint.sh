#!/bin/bash

# Wait for the database to be ready with retries
until nc -z -v -w30 db 5432; do
  echo "Waiting for database connection..."
  sleep 5
done

# Run migrations
python manage.py migrate

# Start the application
exec "$@"