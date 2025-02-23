ARG PYTHON_VERSION=3.13-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi
COPY . /code

ENV SECRET_KEY "7gumcUcqQSoXD6Q41rIi714rmIwUNwoIJ0Lv6urjWJCHf9R5z4"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "poetry shell && gunicorn junbun.wsgi:application --bind 0.0.0.0:8000"]
