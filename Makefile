SHELL := /bin/bash
APP_DIR := .
VENV := ./.venv
BIN := $(VENV)/bin
PYTHON := $(BIN)/python

# vars could be put into external .env file
#include .env

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

.PHONY: create_staticfiles
create_staticfiles: ## Create 'staticfiles' folder
	mkdir staticfiles

.PHONY: run
run: ## Run the Django server
	$(PYTHON) $(APP_DIR)/manage.py runserver

bootstrap: install migrate extract_images load_data create_staticfiles ## Bootstrap the app, install, migrate, add images, load initial data

start: install migrate run ## Install requirements, apply migrations, then start development server

.PHONY: load_data
load_data: wipe_data ## Load data from fixture into DB
	$(PYTHON) $(APP_DIR)/manage.py loaddata pages

.PHONY: wipe_data
wipe_data: ## Remove data of models from the DB
	$(PYTHON) $(APP_DIR)/manage.py wipe_data

.PHONY: extract_images
extract_images: ## Download apps images to static/img folder
	tar xf thumbs.tar.gz --directory=static/img/
	tar xf scans.tar.gz --directory=static/img/

.PHONY: clean
clean: ## Remove the virtual env
	rm -rf $(VENV)
