import os  # pragma: no cover
from datetime import datetime  # pragma: no cover
from dotenv import load_dotenv  # pragma: no cover
from db_setup import setup_db  # pragma: no cover
from db_clean_up import clean_up_db  # pragma: no cover

load_dotenv(".flaskenv")  # pragma: no cover
load_dotenv()  # pragma: no cover
# Generate unique DB_NAME for testing:
db_name = os.environ.get("DB_NAME", "haski")
db_name = (
    db_name
    + "_test"
    + datetime.now().strftime("%Y%m%d%H%M%S")
    + str(os.getpid())
)  # pragma: no cover
os.environ.update(
    {
        "DB_NAME": db_name,
    }
)  # pragma: no cover
print("DB_NAME: {}".format(os.environ.get("DB_NAME")))  # pragma: no cover

print("Setting up DB...")  # pragma: no cover
setup_db(db_database=db_name)  # pragma: no cover

print("Running tox...")  # pragma: no cover
os.system("tox")  # pragma: no cover

print("Cleaning up DB...")  # pragma: no cover
clean_up_db(db_database=db_name, db_drop=True)  # pragma: no cover

print("isort check...")  # pragma: no cover
os.system("isort --check-only .")  # pragma: no cover

print("Flake8...")  # pragma: no cover
os.system("flake8")  # pragma: no cover

print("Black check...")  # pragma: no cover
os.system("black --check .")  # pragma: no cover

print("Done!")  # pragma: no cover
