import os


def get_postgres_uri():  # pragma: no cover
    host = os.environ.get("DB_HOST", "127.0.0.1")
    port = os.environ.get("DB_PORT", 5432)
    password = os.environ.get("DB_PASSWORD", "postgres")
    user = os.environ.get("DB_USER", "postgres")
    db_name = os.environ.get("DB_NAME", "haski")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():  # pragma: no cover
    host = os.environ.get("API_HOST", "localhost")
    port = 5000 if host == "localhost" else 80
    return f"http://{host}:{port}"
