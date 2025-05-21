# Setting up the API locally

## Set up a Python venv with the required packages

The API currently runs on Python 3.11, so it's advised to create a virtual environment using Python 3.11 and installing all necessary packages for the API there. 

To create a Python 3.11 venv, make sure that you have Python 3.11 installed and that it's in your PATH if you're on Windows (I don't know anything about Mac or Linux). Then you'll want to run the command:

`python3.11 -m venv venv_name`

Run `venv_name\scripts\activate` to activate the virtual environment

With your venv activated, navigate to the api folder in a terminal and run: 

`pip install -r requirements.txt`

## Migrating the db 

In order to get your local db up-to-date, make sure you're on the latest version of the code and run `alembic upgrade head`. This will ensure that all migrations have been applied to your database.

## Seeding the db 

From the root folder (bad-reads) run: 

`python -m api.infrastructure.db.seed`

This will populate the db with a number of books, authors and users which you can use to play around the API with

## Running unit tests 

From either the root or api folder, doesn't really matter, run:

`pytest`

This will run all the unit tests 

## Running the api 

From api run `python -m run`
