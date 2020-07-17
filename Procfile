release: python manage.py migrate --noinput
web: gunicorn boringnotes.wsgi
worker: celery -A notes.tasks worker -B --loglevel=info
