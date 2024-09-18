# docker compose build -f deploy-compose.yml report_service
FROM python:3.11-slim AS base
WORKDIR /app

FROM base AS builder
COPY /report_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM builder AS development
ENTRYPOINT [ "python", "main.py" ]
EXPOSE 50051

FROM builder AS production
COPY report_service/ /app/
ENTRYPOINT [ "python", "main.py" ]
EXPOSE 50051
