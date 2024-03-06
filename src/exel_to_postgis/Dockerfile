FROM python:3.11-slim

WORKDIR /app

COPY ./infra/requirements.extractor.txt ./requirements.txt

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

COPY ./src/core/__init__.py ./src/core/__init__.py
COPY ./src/__init__.py ./src/__init__.py
COPY ./src/core/configs ./src/core/configs
COPY ./src/core/utils ./src/core/utils
COPY ./src/exel_to_postgis ./src/exel_to_postgis

CMD ["python", "-m", "src.exel_to_postgis.load_data"]
