from django.db import models

# Create your models here.

class Notes(models.Model):
    notes_id = models.PositiveIntegerField()
    title = models.CharField(max_length=5000)
    pdf = models.FileField(upload_to="notes")

    class Meta:
        ordering = ['notes_id']

    def __str__(self):
        return str(self.notes_id)