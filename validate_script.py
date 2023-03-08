import os  # pragma: no cover

os.system(
    'pytest --cov=. \
        --cov-report term-missing --envfile .env')  # pragma: no cover
os.system('pycodestyle .')  # pragma: no cover
