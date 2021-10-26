SHELL := /bin/bash
APP_DIR := .
VENV := ./.venv
BIN := $(VENV)/bin
PYTHON := $(BIN)/python

include .env

.PHONY: help
help: ## Show this help
	@grep -Eh '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	python3 -m venv $(VENV) && source $(BIN)/activate && which python

.PHONY: install
install: venv ## Make venv and install requirements
	$(BIN)/pip install -r requirements.txt

migrate: ## Make and run migrations
	$(PYTHON) $(APP_DIR)/manage.py makemigrations
	$(PYTHON) $(APP_DIR)/manage.py migrate

.PHONY: run
run: ## Run the Django server
	$(PYTHON) $(APP_DIR)/manage.py runserver

start: install migrate run ## Install requirements, apply migrations, then start development server

.PHONY: load_data
load_data: ## Load data from fixture into DB
	$(PYTHON) $(APP_DIR)/manage.py loaddata pages

.PHONY: wipe_data
wipe_data: ## Remove data of models from the DB
	$(PYTHON) $(APP_DIR)/manage.py wipe_data

.PHONY: clean
clean: ## Remove the virtual env
	rm -rf $(VENV)
