# docker compose -f deploy-compose.yml build rest-proxy

FROM python:3.11-slim AS base
WORKDIR /code


FROM base AS builder
COPY rest_proxy/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM builder AS development
# Use the volume directive in the compose.yml file to mount the files
ENTRYPOINT fastapi dev main.py
EXPOSE 8000


FROM builder AS production
COPY rest_proxy/. .
ENTRYPOINT fastapi run main.py
EXPOSE 8000
