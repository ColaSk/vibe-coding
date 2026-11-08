.PHONY: check test fmt

check:
	uv run ruff format --check .
	uv run ruff check .
	uv run mypy app tests
	uv run lint-imports
	uv run pytest

test:
	uv run pytest

fmt:
	uv run ruff format .
	uv run ruff check --fix .
