.PHONY: help hello lint sort format check

# Files to operate on (default: current directory). Override with e.g.
# `make lint FILES=project-2/books.py`
FILES ?= .

help:
	@echo "Usage: make [target] [FILES=path]"
	@echo "Targets:"
	@echo "  hello            - print hello"
	@echo "  lint             - run ruff check --fix on $(FILES)"
	@echo "  sort             - run ruff import sorting (ruff) on $(FILES)"
	@echo "  format           - run ruff format on $(FILES)"
	@echo "  check            - format then lint"

hello:
	@echo "Hello World"
	@echo "This is a second line"

# Lint (auto-fix when possible). Uses `python -m ruff` for portability.
lint:
	uv run ruff check $(FILES) --fix

# Run only import-sorting fixes (select code: I)
sort:
	uv run ruff check --select I $(FILES) --fix

# Format code (ruff formatter)
format:
	uv run ruff format $(FILES)

check: format lint

# End of Makefile