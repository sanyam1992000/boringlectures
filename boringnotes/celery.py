from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boringnotes.settings')

app = Celery('boringnotes')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
from django.conf import settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# worker: python manage.py celery worker -B -l info
# worker: celery worker --app=tasks.app
# worker: REMAP_SIGTERM=SIGQUIT celery worker --app boringnotes.celery.app --loglevel info
# worker: REMAP_SIGTERM=SIGQUIT celery -A boringnotes worker -l info

# worker: celery -A notes.tasks worker -B --loglevel=info
