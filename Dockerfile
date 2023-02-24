# syntax=docker/dockerfile:1

FROM python:3.10.4-slim-buster

RUN addgroup -S nonroot \
    && adduser -S nonroot -G nonroot

USER nonroot


WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]