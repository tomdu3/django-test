# django-test

Here's a django repository that I'm using to test out some new features.

## Installation


```bash
git clone https://github.com/tomdu3/django-test.git
cd django-test
```
Activate  your virtualenv or install it in one of the following ways:
```bash
python3 -m venv venv
source venv/bin/activate
```

or

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Then install the requirements:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://localhost:8000 in your browser.


## Features

- send email helper function