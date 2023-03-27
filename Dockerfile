FROM python:3.8.16

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./src /app/src

COPY ./main.py /app

COPY ./reference /app/reference

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --reload