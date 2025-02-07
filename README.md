# URL Shortener


```markdown

A simple URL shortener built using Django, DRF, PostgreSQL, and Docker. This project allows users to shorten URLs and retrieve them using a unique short code.

## Features
- URL shortening: Users can shorten any URL into a short code.
- URL redirection: Users can access the original URL by visiting the shortened URL.
- Dockerized setup: The project is set up to run using Docker for easy development and deployment.

## Tech Stack
- **Backend**: Django, DRF, Python 3.10.12
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Web Server**: Nginx

## Requirements
- Docker
- Docker Compose

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/babarakshay2019/url_shortener.git
cd url_shortener
```

### Step 2: Build the Docker Containers
```bash
docker compose up --build
```

This command will build and start the `web`, `db`, and `nginx` containers.

### Step 3: Access the Application
Once the containers are running, you can access the application by visiting `http://localhost` in your browser.

### Step 4: Create a Superuser
To create a superuser for accessing the Django admin panel, run:
```bash
docker compose exec web python manage.py createsuperuser
```

### Step 5: Migrate the Database
To apply database migrations, run:
```bash
docker compose exec web python manage.py migrate
```

## Usage
- **Shorten a URL**: Navigate to the URL shortening page and input the URL you wish to shorten.
- **Access a Shortened URL**: Visit `http://localhost/<short-code>` to be redirected to the original URL.

## Docker Commands

- To start the project (in detached mode):
  ```bash
  docker compose up -d
  ```

- To stop the project:
  ```bash
  docker compose down
  ```
