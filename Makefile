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
        docker-compose run web ./manage.py shell -c "from users.models import User; User.objects.create_superuser('admin@admin.com', 'admin')"

loaddata:
        docker-compose run web ./manage.py loaddata ./staging-fixtures/breed.json ./staging-fixtures/cities.json ./staging-fixtures/sites.json ./staging-fixtures/socialapp.json
