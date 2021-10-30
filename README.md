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


## Project business requirements
### Users vs People
- We need users to access the app with email and password -> this will be Django Users
- We need to have records of different kind of people roles: Players, Coaches, Player's parents, Club members (socis), Staff (Board members, Coordinator, Account...), Sponsor
- We could have someone that's Staff, Player, Parent and Coach at the same time. Also, they may need access to the platform.

### Tables
- We need a table to see every team, its players and coaches. A player can be in more than one team. This needs to be different for every season, but we want to move players from one season to another.
- We need a table to see which player has paid their monthly/yearly quota.
- We need a table to see which player has paid their equipment fee.
- We need a table to see which sponsor has paid their contribution.
- We need a table to see the payrolls for Staff and Coaches.

### Imports / Exports
- Initial data may come from excels files.
- Tables may need to be exported to excel/CSV.

### Notifications
- They want to notify staff when a payment due date arrives. We could also notify the affected person directly if they have an email.

### Suggestions
- Integration with Stripe / Paypal for online payments.
