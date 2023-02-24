import os


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", 0)
    password = os.environ.get("DB_PASSWORD", "")
    user = os.environ.get("DB_USER", "")
    db_name = os.environ.get("DB_NAME", "")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5000 if host == "localhost" else 80
    return f"https://{host}:{port}"
