FROM python:3.11.4-slim

WORKDIR /app

COPY report_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY report_service/. .
COPY proto/ proto/

EXPOSE 50051

CMD ["python", "main.py"]
