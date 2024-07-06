# Example python project

This is a demo project for django with a rest API using a postgresql database.

## Requirements

Here are the tools you need to run this project :
 - Python
 - Docker + Docker compose

## Setup

### Create a virtual environment

```sh
python -m venv venv
```

### Activate the virtual environment

```sh
.\venv\Scripts\activate # Windows powershell
source ./venv/bin/activate # Linux and Mac
```

### Install dependencies

```sh
pip install -r ./requirements/dev.txt
```

## Load environment variables

This project requires environment variables to be configured in order to run. The list is avaialable at the end of this
document. You can also see a list of variables in the .env.example file.

There are multiple ways to load variables in your terminal depending on your OS, so feel free to do it however you please.

## Run the database

While working in a local environment, you can use the compose file provided to run a database.

```shell
docker compose up -d
```

## Run migrations

Migrations will apply the necessary scripts to setup your database and apply changes made in your models.

```shell
python ./manage.py migrate
```

## Load initial data

```shell
python ./manage.py loaddata ./fixtures/articles.json
```

## Run a local development server

```shell
python ./manage.py runserver
```

## Run the server in production mode

You can use the provided script `start.sh` to run a production instance. It will wait for the database to be ready,
apply migrations and then load inital data. This script should be ran inside a Dockerfile.

## List of available environment variables

- `DATABASE_HOST`: The hostname to access your database
- `DATABASE_PORT`: The port to access your database
- `DATABASE_USER`: The username to access your database
- `DATABASE_PASSWORD`: The password to access your database
- `DATABASE_NAME`: The name of the database
