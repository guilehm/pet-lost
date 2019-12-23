lint:
	@flake8
	@isort --check

test:
	flake8
	isort
	py.test -v

test-docker:
	docker-compose run web make test

superuser:
	./manage.py shell -c "from users.models import User; User.objects.create_superuser('admin@admin.com', 'admin')"

superuser-docker:
	docker-compose run web ./manage.py shell -c "from users.models import User; User.objects.create_superuser('admin@admin.com', 'admin')"