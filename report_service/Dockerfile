FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# TODO: is it needed to re-create the servicers from protofiles here?

EXPOSE 50051

CMD ["python", "main.py"]
