# Edu Platform

This is an educational platform built with Django, Celery, RabbitMQ, and PostgreSQL. The platform supports real-time stock updates and asynchronous task processing.

## Project Setup

### Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose
- Python 3.8+

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sirojiddinov07/EduDemo.git
   cd edu-platform
   ```

2. Create an `.env` file based on `.env.example` and configure the environment variables.

3. Build and start the Docker containers:

   ```bash
   docker compose up -d --build
   ```

4. Run database migrations:

   ```bash
   docker compose exec web python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```


### Services

The application consists of the following services:

- **Web**: Django application (`edu-web`)
- **Database**: PostgreSQL (`edu-db`)
- **Celery Worker**: Handles background tasks (`edu-celery_worker`)
- **Celery Beat**: Manages periodic tasks (`edu-celery_beat`)
- **RabbitMQ**: Message broker for Celery (`edu-rabbitmq`)

### Managing Containers

To stop all containers:

```bash
docker compose down
```

To restart the services:

```bash
docker compose up -d
```

### Logs & Debugging

To check logs for a specific service:

```bash
docker compose logs -f web
```

To open an interactive shell inside the Django container:

```bash
docker compose exec web bash
```

## API Endpoints

To check available API endpoints, visit:

```
http://localhost:8000/api/docs/
```


