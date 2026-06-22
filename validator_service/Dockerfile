FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install uv && uv pip install --system .

COPY . .

CMD ["faststream", "run", "app.main:app", "--workers", "4"]