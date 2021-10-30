# General Manager

Sport Club platform to manage players, payments, sponsors...

## Installation

Make sure you have installed in your OS
```
make
python3.6
virtualenv
postgresql
```

Create a PostgreSQL database
```
sudo su - postgres
psql
CREATE DATABASE general-manager;
CREATE USER general-manager WITH PASSWORD 'general-manager';
GRANT ALL PRIVILEGES ON DATABASE general-manager TO general-manager;
ALTER USER general-manager CREATEDB;
```

Then run:
```
make requirements
make virtualenv
source venv/bin/activate
cd src/
./manage.py migrate
```

## Run tests

Run `make tests`. It will do isort-check, lint and django tests.

## Utils

Update packages: `make requirements`. Creates a requirements.txt file with the last versions of the packages inside requirements/base.txt. You can run it whenever you want to update your project. It will create a temporary virtualenv.

`make virtualenv` Creates a new virtualenv using requirements.txt.

`make clean` Removes the .pyc files and deletes the virtualenv folder.

`make isort` Checks your code and fixes the imports using isort.
