# django-test

Here's a django repository that I'm using to test out some new features.

## Installation

## Docker Installation instructions

### Start the server

- Run `docker compose up --build` to start the server. Depending on the docker compose installation, you may need to run it as `docker-compose` and not `docker compose`.

- To interact with the database, you can use:

```bash
docker compose exec db psql -U <USERNAME> -d <DATABASE_NAME>
```

- To interact with the django-test server in shell, you can use:

```bash
 docker exec -ti <APP_NAME> ./manage.py shell
```

### Remove the server

- Run `docker compose down -v`, or `docker-compose down -v` to remove the server.

## Old Installation Instructions

- For Python environment, we are using [uv](https://docs.astral.sh/uv/guides/install-python/) to run the server.

- There's a [.env.example](.env.example) file that you can copy to `.env` and fill in the values for your environment variables.

- Run `uv run manage.py runserver` to start the server. If you don't have python environment installed, it will install it automatically.
- When everything is ready, you will see a message similar to this:

```
Django version 3.2.3, using settings 'test.settings'
Starting development server at http://localhost:8000/
Quit the server with CONTROL-C.
```

Then open <http://localhost:8000> in your browser.

## Features

- send email helper function
