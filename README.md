# Backend

Stack:
- Django
- Django Rest Framework
- PostgreSQL
- Pytest
- Nginx
- Docker Compose

# URL's path

Base url: `http://localhost`

Admin url: `http://localhost/admin/`

Api: `http://localhost/api/`

Swagger: `http://localhost/api/swagger/`

# Admin user data

l: `admin@example.com`

p: `password`

## Install with docker
### First Run
```sh
docker compose build

docker compose up
```

### Run tests

```sh
docker exec -it web pytest
```

### Run flake8

```sh
docker exec -it web flake8 .
```

### Run mypy

```sh
docker exec -it web mypy .
```

## Install with Venv
My recomendation - run from docker. 
- Add env key for run in local
- Create venv. `python -m venv venv`
- Activate venv. `source venv/bin/activate`
- Run migrations. `python manage.py migrate`
- Runserver. `python manage.py runserver`

### Run Tests
```sh
pytest
```

### Run flake8 . 
```sh
flake8 .
```
