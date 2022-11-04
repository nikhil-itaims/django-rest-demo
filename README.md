# Django Rest Framework demo

Django project setup with complete rest apis demo

## How to run project

Clone project

### For ubuntu system

Create virtual environment

```bash
python3 -m venv venv
```

Activate virtual environment and install all dependancies

```bash
. venv/bin/activate
```

```bash
pip install django
pip install djangorestframework
```

Apply all migrations to migrate  

```bash
python3 manage.py migrate
```

Now you can test the app using development server

```bash
python3 manage.py runserver
```

### For windows system

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment and install all dependancies

```bash
venv/Scripts/activate
```

```bash
pip install django
pip install djangorestframework
```

Apply all migrations to migrate  

```bash
python manage.py migrate
```

Now you can test the app using development server

```bash
python manage.py runserver
```
