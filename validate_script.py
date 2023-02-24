import os

os.system('pytest --cov=. --cov-report term-missing --envfile .env')
os.system('pycodestyle .')
