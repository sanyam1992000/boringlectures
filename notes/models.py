from django.db import models

# Create your models here.

class Notes(models.Model):
    notes_id = models.PositiveIntegerField()
    title = models.CharField(max_length=5000)
    pdf = models.FileField(blank=True, null=True, upload_to="notes")
    date_time = models.DateTimeField(blank=True, null=True)
    total_pages = models.PositiveIntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['notes_id', 'date_time']

    def __str__(self):
        return str(self.notes_id)