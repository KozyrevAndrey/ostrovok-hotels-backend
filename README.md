# Backend

Stack:
- Django
- Django Rest Framework
- PostgreSQL
- Pytest
- Nginx
- Docker Compose

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
