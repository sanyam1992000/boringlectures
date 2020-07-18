release: python manage.py migrate --noinput
web: gunicorn boringnotes.wsgi
worker: celery worker --app=celery.app
