#!/usr/bin/bash
poetry run coverage erase && \
	poetry run coverage run --source src --branch -m pytest . && \
	poetry run coverage html && \
	poetry run coverage report -m && \
    poetry run black .
