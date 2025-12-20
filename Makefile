.PHONY: help hello lint sort format check run

# Files to operate on (default: current directory). Override with e.g.
# `make lint FILES=project-2/books.py`
FILES ?= .
MODULE_NAME =

# MODULE_NAME has to be provided manually

help:
	@echo "Usage: make [target] [FILES=path] [MODULE_NAME=module]"
	@echo "Targets:"
	@echo "  hello            - print hello"
	@echo "  lint             - run ruff check --fix on $(FILES)"
	@echo "  sort             - run ruff import sorting (ruff) on $(FILES)"
	@echo "  format           - run ruff format on $(FILES)"
	@echo "  check            - format then lint"
	@echo "  run			  - run Uvicorn FastAPI server for module $(MODULE_NAME)"

hello:
	@echo "Hello World"
	@echo "This is a second line"

print:
	@echo "MODULE_NAME = '$(MODULE_NAME)'"

# Lint (auto-fix when possible). Uses `python -m ruff` for portability.
lint:
	uv run ruff check $(FILES) --fix

# Run only import-sorting fixes (select code: I)
sort:
	uv run ruff check --select I $(FILES) --fix

# Format code (ruff formatter)
format:
	uv run ruff format $(FILES)

check: sort format lint

# Run Uvicorn FastAPI server
run:
	uv run uvicorn $(MODULE_NAME):app --reload

# Run PyTest
test:
	uv run pytest

# End of Makefile