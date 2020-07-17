release: python manage.py migrate --noinput
web: gunicorn boringnotes.wsgi
worker: python manage.py celery worker -B -l info
