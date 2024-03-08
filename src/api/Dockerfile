FROM python:3.11-slim

WORKDIR /APP

COPY ./infra/requirements.api.txt ./requirements.txt

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

COPY ./src/api ./src/api
COPY ./src/core ./src/core
COPY ./src/__init__.py ./src

CMD ["uvicorn", "src.api.main:api", "--host", "0.0.0.0", "--port", "8000"]
