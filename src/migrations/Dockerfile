FROM python:3.11-slim

WORKDIR /app

COPY ./infra/requirements.migrations.txt ./requirements.txt

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

COPY ./src/core/db/models ./src/core/db/models
COPY ./src/core/db/__init__.py ./src/core/db/__init__.py
COPY ./src/core/configs ./src/core/configs
COPY ./src/migrations ./src/migrations
COPY ./alembic.ini ./

CMD ["alembic", "upgrade", "head"]
