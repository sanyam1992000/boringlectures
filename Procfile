release: python manage.py migrate --noinput
web: gunicorn boringnotes.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery -A boringnotes worker -l info
