FROM python:3.11.0b1-slim-buster
COPY ./ ./app

WORKDIR /app/

# install project dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -e .
RUN pip install gunicorn

CMD gunicorn api.wsgi:application --bind 0.0.0.0:$PORT