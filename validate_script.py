import os  # pragma: no cover

# start the flask app in the background as
# long as the pytest command is running
# flask run in the background
# windows
os.system("start /B flask run")  # pragma: no cover
# linux
# os.system('python app.py &')  # pragma: no cover
os.system("timeout 5")  # pragma: no cover
# run the tests
os.system(
    "pytest --cov=. \
        --cov-report term-missing --envfile .env"
)  # pragma: no cover
# stop the flask app
# windows
os.system("taskkill /F /IM python.exe")  # pragma: no cover
# linux
# os.system('pkill -f app.py')  # pragma: no cover
# run the linter
os.system("pycodestyle .")  # pragma: no cover
