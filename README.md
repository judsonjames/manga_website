# We Make Manga (WMM) Website

## How to Run
- This project uses Django and Pipenv, a Pip virtual environment for Python.
- In order to run this website:
  ```
  pipenv run python3 manage.py runserver
  ```
- In order to run this application from a fresh clone:
  ```
  # Gets the pipenv enviroment set up for your local machine
  pipenv sync

  # Gets database set up for local testing
  pipenv run python3 manage.py makemigrations
  pipenv run python3 manage.py migrate
  ```

- In order to backup data from the database:
  ```
  pipenv run python3 manage.py dumpdata --exclude=auth --exclude=contenttypes --exclude=admin --exclude=sessions > navigation/fixtures/dump.json
  ```

- In order to load data from the dump.json:
  ```
  pipenv run python3 manage.py loaddata navigation/fixtures/dump.json
  ```
