FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.9.8 /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY app ./app

ENV PYTHONPATH=/app
EXPOSE 8000
CMD ["uv", "run", "--frozen", "--no-dev", "fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
