import os
import db_config


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = db_config.port
    password = os.environ.get("DB_PASSWORD", db_config.password)
    user, db_name = db_config.user, db_config.db_name
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5000 if host == "localhost" else 80
    return f"http://{host}:{port}"
