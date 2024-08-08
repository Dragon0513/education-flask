# syntax=docker/dockerfile:1

# Stage 1: Build stage
FROM python:3.10.4-slim-buster AS builder

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

# Stage 2: Final stage
FROM python:3.10.4-slim-buster

WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application files
COPY domain/ /app/domain/
COPY entrypoints/ /app/entrypoints/
COPY repositories/ /app/repositories/
COPY service_layer/ /app/service_layer/
COPY setup/ /app/setup/
COPY tests/ /app/tests/
COPY utils/ /app/utils/
COPY config.py /app/config.py
COPY errors/ /app/errors/

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
