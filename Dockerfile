# syntax=docker/dockerfile:1

# Builder stage
FROM python:3.10.4-slim-buster AS builder

WORKDIR /build
COPY ./requirements.txt /build/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the source code and other necessary files
COPY domain/ /build/domain/
COPY entrypoints/ /build/entrypoints/
COPY repositories/ /build/repositories/
COPY service_layer/ /build/service_layer/
COPY setup/ /build/setup/
COPY tests/ /build/tests/
COPY utils/ /build/utils/
COPY config.py /build/
COPY errors/ /build/errors/

# Runtime stage
FROM python:3.10.4-slim-buster AS runtime

WORKDIR /app
COPY --from=builder /build /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
