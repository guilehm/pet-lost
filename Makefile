DOCKER_COMPOSE=docker-compose
DOCKER_COMPOSE_RUN=docker-compose run web

lint:
	-$(DOCKER_COMPOSE_RUN) bash -c "flake8 && isort --check"

migrate:
	-$(DOCKER_COMPOSE_RUN) ./manage.py migrate

test:
	-$(DOCKER_COMPOSE_RUN) pytest -vv

superuser:
	-$(DOCKER_COMPOSE_RUN) ./manage.py shell -c "from users.models import User; User.objects.create_superuser('admin@admin.com', 'admin')"

loaddata:
	-$(DOCKER_COMPOSE_RUN) ./manage.py loaddata ./staging-fixtures/breed.json ./staging-fixtures/cities.json ./staging-fixtures/sites.json ./staging-fixtures/socialapp.json

setup:  migrate superuser loaddata

run:
	-$(DOCKER_COMPOSE) up
