# syntax=docker/dockerfile:1

FROM python:3.10.4-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

#Copying only needed folders/files to image

COPY domain/ /app/domain/

COPY entrypoints/ /app/entrypoints/

COPY repositories/ /app/repositories/

COPY service_layer/ /app/service_layer/

COPY setup/ /app/setup/

COPY tests/ /app/tests/

COPY .flaskenv /app/

COPY config.py /app/

COPY errors.py /app/

COPY requirements.txt /app/

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]