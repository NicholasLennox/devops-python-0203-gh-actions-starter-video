# PriceFixers Tasks API

A small internal task tracking API built by the PriceFixers team.

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
# Mac and Linux
source venv/bin/activate

# Windows - Git Bash
source venv/Scripts/activate

# Windows - Command Prompt
venv\Scripts\activate

# Windows - PowerShell
venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in the values:

```bash
cp .env.example .env
```

## Running the Tests

```bash
python -m pytest
```

## Running the API

Mac and Linux:

```bash
gunicorn --bind 0.0.0.0:8000 src.app:app
```

Windows:

```bash
FLASK_APP=src/app.py flask run
```

## Docker

Build the image:

```bash
docker build -t tasks-api .
```

Run the container:

```bash
docker run -d -p 9000:8000 --env-file .env tasks-api
```

Run the tests inside the container:

```bash
docker run --env-file .env tasks-api python -m pytest
```

Tag and push to Docker Hub:

```bash
docker tag tasks-api your-dockerhub-username/tasks-api:latest
docker push your-dockerhub-username/tasks-api:latest
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check - returns environment info |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get a task by ID |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| ENVIRONMENT | Environment name | development |

See `.env.example` for the expected format.