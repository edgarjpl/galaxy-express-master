web_cmd = docker-compose run web
ini_file = /src/configs/development.ini

.PHONY: test
test:
	$(web_cmd) python -m pytest -v

.PHONY: shell
shell:
	$(web_cmd) baseplate-shell $(ini_file)

.PHONY: migratedb
migratedb:
	$(web_cmd) baseplate-script $(ini_file) galaxy_express.models:create_schema

.PHONY: dropdb
dropdb:
	$(web_cmd) baseplate-script $(ini_file) galaxy_express.models:drop_schema

.PHONY: resetdb
resetdb: dropdb migratedb
