#!/usr/bin/env just --justfile

# Show this help
list:
    just --list


# Setup
install:
    @uv sync
    @uv pip install -e .
    @uv run pre-commit install


# Check formatting and syntax
check:
    @uv run pre-commit run --all-files


# Format code with Ruff
format:
    @uv run ruff check --fix
    @uv run ruff format


# Run mypy
mypy:
    @uv run mypy .


# Run development server
dev:
    @uv run python scripts/dev.py


# Create static site in /build
build:
    @uv run python scripts/build.py


# Fetch the latest data
fetch:
    @uv run python scripts/scrape_event_data.py


# Push to remote
push:
    @git push --set-upstream origin `git rev-parse --abbrev-ref HEAD`
