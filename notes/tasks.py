from celery import shared_task
from time import sleep
from background_task import background
from .models import Notes

@background(schedule=10)
def sleepy():
    notes = Notes.objects.create(title="testings fkcrepc", notes_id=12)
    return None