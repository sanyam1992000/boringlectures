release: python manage.py migrate --noinput
web: gunicorn boringnotes.wsgi
worker: celery -A boringnotes.tasks worker -B --loglevel=info
