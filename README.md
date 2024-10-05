# Setup

As I used to not write documentation, I must now do some deep digging to find out how to make it work, almost 10 years (!!!) after.


## Python

First get the relevant Python version (as I used Django 1.8.x the documentation says its compatible with Python 3.5)

```bash
pyenv install -v 3.5.10
pyenv virtualenv 3.5.10 DjangoMap3.5
pyenv local DjangoMap3.5
```

.python-version file at the root of the project now contains the name of the related pyenv.

## Packages

As everything changes, you must install the requirements this way (check by yourself don't ask me why) :
`pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt`

## Django

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Database

I made some save of my old travel DB, just find it and replace the SQlite file as I used it in production (lol).
Same for the media, the save is in the same place on gdrive.
