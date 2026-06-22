runserver:
	uvicorn app.main:app --host localhost --port 8003 --reload

lint:
	uv run ruff check

migarate:
	alembic upgrade head

up:
	docker compose up

install:
	uv sync