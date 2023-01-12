import os

os.system('pytest --cov=. --cov-report term-missing')
os.system('pycodestyle .')
