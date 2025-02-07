FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy requirements file and tnstall dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -xzvf dockerize-linux-amd64-v0.6.1.tar.gz \
    && mv dockerize /usr/local/bin/

RUN apt-get update && apt-get install -y netcat-openbsd

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint to the script
ENTRYPOINT ["/entrypoint.sh"]

# Copy project files to the container
COPY . .

# RUN chmod -R 755 /app/logs
RUN mkdir -p /app/logs && chmod -R 755 /app/logs

# EXPOSE post 8000 for the django application
EXPOSE 8000

# Run Django application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "url_shortener.wsgi:application"]