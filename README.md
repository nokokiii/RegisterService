# Register Service

The Register Service is designed to store and manage information about users.

## Create a virtual environment

```commandline
python -m venv ./.venv
```

### Activate virtual environment (for Windows)

```commandline
./.venv/Scripts/activate
```

### Install Requirements

```commandline
pip install -r ./requirements.txt
```

## Set up Database and .env

### Installing SurrealDB on Windows

Here are the docs for [Installing SurrealDB on Windows](https://docs.surrealdb.com/docs/installation/windows)

### Starting SurrealDB Database

```commandline
surreal start --log trace --user username --pass password --bind 0.0.0.0:9000 --auth memory
```

### Create .env file

Create a .env file in the root directory of the project and add the following

```
USER=username
PASSWORD=password
NAMESPACE=namespace
DATABASE=database
```

## Run the application

Run Flask application

```commandline
py -m src.app
```

## Testing

Run tests

```commandline
py -m src.tests.run_tests
```

## Authors

- [nokokiii](https://github.com/nokokiii)

