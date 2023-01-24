FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8080
EXPOSE 5000

CMD ["flask", "--app", "hello",  "run", "--host=0.0.0.0"]
