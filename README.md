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

## Resources

### Articles/Docs

- [Django documentation](https://docs.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker documentation - Startup Order](https://docs.docker.com/compose/how-tos/startup-order/)
- [DockerHub - Postgres](https://hub.docker.com/_/postgres)
- [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/)
- [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
- [How to Set Up a Currency Converter in Django?](https://www.horilla.com/blogs/how-to-set-up-a-currency-converter-in-django/)
- [Building a Currency Converter in Django: A Step-by-Step Guide](https://dev.to/rohitashsingh89/building-a-currency-converter-in-django-a-step-by-step-guide-560f)

### Videos

- [BugBytes: Docker - Django and PostgreSQL setup (with uv) from scratch!](https://youtu.be/37aNpE-9dD4)
