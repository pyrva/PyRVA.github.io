#!/usr/bin/env just --justfile

# Show this help
list:
    just --list


# Setup
install:
    poetry install
    poetry run pre-commit install


# Check formatting and syntax
check:
    @poetry run pre-commit run --all-files


# Format code with Ruff
format:
    @ruff check --fix
    @ruff format


# Run mypy
mypy:
    @poetry run mypy .


# Create static site in /build
build:
    @poetry run python src/pyrva/freezer.py


# Push to remote
push:
    @git push --set-upstream origin `git rev-parse --abbrev-ref HEAD`
