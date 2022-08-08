FROM python:3.8

ENV PYTHONPATH "${PYTHONPATH}:/"

RUN pip install --upgrade pip

COPY ./requirements.txt .

COPY ./app /app

COPY ./models /models

COPY ./controller /controller

COPY ./database /database

COPY main.py main.py

COPY .env .env

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
