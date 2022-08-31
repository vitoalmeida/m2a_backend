FROM python:3.11.0b1-slim-buster
COPY ./ ./app

WORKDIR /app/

# install project dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -e .
