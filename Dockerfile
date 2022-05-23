FROM python:slim

WORKDIR /app

#Poetry
RUN pip install poetry
ADD pyproject.toml .
ADD poetry.lock .
RUN poetry config virtualenvs.create false
RUN poetry install

ADD api api

CMD uvicorn api:app --host ${SERVER_HOST} --port ${SERVER_PORT} --log-level=warning