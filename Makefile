lint:
	@flake8
	@isort --check

test:
	flake8
	isort
	py.test -v

testdocker:
	docker-compose run web make test
