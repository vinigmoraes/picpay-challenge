FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app
ARG PORT=8080

RUN apk update && apk upgrade
RUN apk add gcc python3-dev libc-dev gpgme-dev

RUN mkdir /app

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r /app/requirements.txt

COPY . /app/

CMD ["python" , "main.py"]

EXPOSE ${PORT}
