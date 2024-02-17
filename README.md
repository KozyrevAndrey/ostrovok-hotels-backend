# Backend

### First Run
```sh
docker compose build

docker compose up
```

### Run tests

```sh
# if you run in docker compose
docker exec -it web pytest
```

### Run flake8

```sh
# if you run in docker compose
docker exec -it web flake8 .
```

### Run mypy

```sh
# if you run in docker compose
docker exec -it web mypy .
```
