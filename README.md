# django-with-vuejs

Fast and clear in DevOps. [中文 README.md](/README-zh.md)

Simple is better.

> Why [Django Project](/examples/django-auth-with-react/backend) dir and [Frontend](/examples/django-auth-with-react/frontend) dir are the same level in [example/django-auth-with-react](/examples/django-auth-with-react) dir，but it's not in [project](/project) dir?

That is because the django-auth-with-react project is completely a front-end separation project.

### Step 1: Install frontend dependencies

In the directory where the package.json file is located

```bash
cd django-with-vuejs/my_project/vue2_frontend
npm install
```

### Step 2: Build the front end

In the frontend directory

```bash
npm run build
```

### Step 3: Start the project with Django's own server

In the directory where manage.py is located

```bash
pip install -r requirements.txt
python manage runserver
```

All done.

---

but if you want to know the principle, keep reading

## Principle

- index.html
- static/\*

### First. index.html

Handle the `index.html` file with [django template engines](https://docs.djangoproject.com/en/dev/topics/templates/)

In `settings.py`

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': ['vue2_frontend/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

We change the `TEMPLATES.DIRS` so that _django template engines_ know where to find the **index.html**.

### Second. static/\*

In `settings.py`

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "vue2_frontend/dist/static"),
]
```

We add `STATICFILES_DIRS` setting in settings.py, this can make django find the resource

```html
<script type=text/javascript src=/static/js/vendor.677ef0c9485c32b4f6a9.js></script>
```

in _vue2_frontend/dist/static_ directory, but it worked only in debug mode.

---

## Production

We use Nginx to handle the frontend:

- index.html
- static/\*

Django only handle the API which transport data with JSON.

---

## Any questions?

[New issues](https://github.com/tmpbook/django-with-vuejs/issues/new)
