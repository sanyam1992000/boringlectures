import os
from django.shortcuts import render
from . import get_pdf
from . import models
from django.core.files import File
# Create your views here.

# h = get_pdf.pdf("")

def get_notes(request, content_id):

    f = get_pdf.pdf(str(content_id))
    f = File(f)
    filename = str(content_id) + ".pdf"
    notes = models.Notes.objects.create(notes_id=content_id, title="hello", pdf=f)
    notes.save()
    os.remove(filename)
    return render(request, "home.html")
