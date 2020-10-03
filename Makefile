DOCKER_COMPOSE=docker-compose
DOCKER_COMPOSE_RUN=docker-compose exec web

lint:
	-$(DOCKER_COMPOSE_RUN) bash -c "flake8 && isort --check"

migrate:
	-$(DOCKER_COMPOSE_RUN) ./manage.py migrate

test:
	@echo "Starting tests"
	-$(DOCKER_COMPOSE_RUN) pytest -vv

superuser:
	@echo "Creating superuser admin@admin.com / admin"
	-$(DOCKER_COMPOSE_RUN) ./manage.py shell -c "from users.models import User; User.objects.create_superuser('admin@admin.com', 'admin')"

loaddata:
	@echo "Loading fixtures"
	-$(DOCKER_COMPOSE_RUN) ./manage.py loaddata ./staging-fixtures/breed.json ./staging-fixtures/cities.json ./staging-fixtures/sites.json ./staging-fixtures/socialapp.json

run:
	-$(DOCKER_COMPOSE) up

up:
	-$(DOCKER_COMPOSE) up -d

stop:
	@echo "Stopping containers"
	-$(DOCKER_COMPOSE) stop

down:
	@echo "Removing containers and volumes"
	-$(DOCKER_COMPOSE) down -v

build:
	@echo "Building the app"
	-$(DOCKER_COMPOSE) build

setup: up migrate superuser loaddata
