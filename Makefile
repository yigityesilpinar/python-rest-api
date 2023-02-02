SHELL = /bin/bash

.DEFAULT_GOAL := start
TOP_SLOW ?= 3

LOCAL_MAKEFILE ?= local/Makefile

# allow inclusion of custom rules outside version control without requiring it
-include $(LOCAL_MAKEFILE)

.PHONY: help
help:  ## List of available recipes
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start:  ## Start services
	@docker-compose up

.PHONY: build
build:  ## Start services with build
	@docker-compose build


.PHONY: stop
stop:  ## Stop services
	@docker-compose down

.PHONY: status
status:  ## List of running services
	@docker-compose ps

.PHONY: shell
shell:  ## Spawn shell inside python-rest-api container
	@docker-compose exec python-rest-api /bin/sh

.PHONY: logs
logs:  ## View python-rest-api logs
	@docker-compose logs python-rest-api

.PHONY: upgrade_db
upgrade_db: ## Apply db migrations from within the container
	@docker-compose exec python-rest-api poetry run flask db upgrade

.PHONY: upgrade_db test_all
test_all:  ## Run all tests
	@docker-compose exec python-rest-api poetry run pytest --durations $(TOP_SLOW) -s tests/**