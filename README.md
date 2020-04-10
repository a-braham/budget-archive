# Budget - A personal financial plan that helps users allocate money.

[![Build Status](https://travis-ci.org/a-braham/budget.svg?branch=master)](https://travis-ci.org/a-braham/budget)
[![Maintainability](https://api.codeclimate.com/v1/badges/56d5a97b0331e38d4b67/maintainability)](https://codeclimate.com/github/a-braham/budget/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/a-braham/budget/badge.svg?branch=master)](https://coveralls.io/github/a-braham/budget?branch=master)

## Vision
- Financial assistant for planing and keeping track of income and expenses.

**Features**: Income, Expenses, Savings, Cash Balances

## Local setup
* Create python virtual environment
```
 $ virtualenv -p python3 env
```
* Install Requirements
```
 $ pip install -r requirements.txt
```
* Create a .env file in the root folder and set variables as in the .env-example

* Create postgres database
```
  $ psql postgres
  postgres=# CREATE USER your-user WITH PASSWORD 'your-password';
  postgres=# ALTER ROLE your-user SET client_encoding TO 'utf8';
  postgres=# ALTER ROLE your-user SET default_transaction_isolation TO 'read committed';
  postgres=# ALTER ROLE your-user SET timezone TO 'UTC';
  postgres=# CREATE DATABASE your-database-name;
  postgres=# GRANT ALL PRIVILEGES ON DATABASE your-database-name TO your-user;postgres=# \q
```

* Run Migrations
```
  $ python manage.py makemigrations
  $ python manage.py migrate
```
* Run Server/ Tests
```
  $ python manage.py runserver or
  $ python manage.py test
```
