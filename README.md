# django-test

Here's a django repository that I'm using to test out some new features.

## Installation

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
