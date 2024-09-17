# docker build -f rest_proxy/Dockerfile . -t ts/reporting/rest-proxy:development --target=production

FROM python:3.11-slim AS base
WORKDIR /code


FROM base AS builder
COPY rest_proxy/requirements.txt .
RUN pip install -r requirements.txt


FROM builder AS development
# Use the volume directive in the compose.yml file to mount the files
ENTRYPOINT fastapi dev main.py
EXPOSE 8000


FROM builder AS production
COPY rest_proxy/main.py rest_proxy/lib/ ./
ENTRYPOINT fastapi run main.py
EXPOSE 8000