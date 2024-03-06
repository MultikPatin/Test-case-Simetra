FROM python:3.11-slim

WORKDIR /app

COPY ./infra/requirements.migrations.txt ./requirements.txt

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

COPY ./src/core/db/entities ./src/core/db/entities
COPY ./src/core/db/__init__.py ./src/core/db/__init__.py
COPY ./src/core/db/postgers_settings.py ./src/core/db/postgers_settings.py
COPY ./src/migrations ./src/migrations
COPY ./alembic.ini ./

CMD ["alembic", "upgrade", "head"]
