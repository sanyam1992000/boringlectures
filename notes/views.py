import os
from django.shortcuts import render
from . import get_pdf
from . import models
from django.core.files import File
import shutil
import requests
import json
import img2pdf
# Create your views here.

# h = get_pdf.pdf("")

def get_notes(request, content_id):

    content_id = str(content_id)
    # notesid = input("content id")
    # content_id = "82"
    # content_id = str(notesid)
    base_url = "https://lecturenotes.in/material/" + content_id
    client = requests.Session()

    cookie = "lnsref=bba61fdf6086c715ef5a2153f399aa40"
    head = {
        "Cookie": cookie,
        'accept': 'text/html,application/xhtml+xml,application/xml',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "TE": "Trailers"
    }
    r = client.get(base_url, headers=head)

    # print(r.text)
    data = r.text
    st = (data.find('csrfToken'))
    cst = (data.find('"', st, len(data) - 1))
    end = data.find('"', cst + 1, cst + 100)
    csrf = ""
    for i in range(cst + 1, end):
        csrf += (data[i])
    # print(csrf)
    page_no = 1
    url = "https://lecturenotes.in/material/" + str(content_id) + "/page-" + str(page_no) + "?noOfItems=30"
    token = "oG7nVEzv4_pjQ4CG2BfDYXjI5M1H-vnUVhZ-lYtRbv4"
    cookie = "lnsref=bba61fdf6086c715ef5a2153f399aa40"
    host = "lecturenotes.in"
    head = {"X-CSRF-Token": csrf,
            #      "Cookie":cookie,
            "host": host,
            'accept': 'text/html,application/xhtml+xml,application/xml',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
    try:
        os.mkdir(os.getcwd() + "/" + str(content_id))
    except OSError:
        # print("Creation of the directory  failed", OSError)
        return None
    next_page = True

    images = []
    while (next_page):
        url = "https://lecturenotes.in/material/" + str(content_id) + "/page-" + str(page_no) + "?noOfItems=30"

        data = client.get(url, headers=head)
        # print(data.content)
        d = json.loads(data.text)
        if (len(d['page']) < 30):
            next_page = False

        img_base_url = "https://lecturenotes.in"
        for pg in d['page']:
            # print(pg['path'])
            r = client.get(img_base_url + pg['path'], headers=head)

            with open(str(content_id) + "/" + str(pg["pageNum"]) + ".jpg", 'wb') as f:
                f.write(r.content)
                images.append(str(content_id) + "/" + str(pg["pageNum"]) + ".jpg")

        page_no += 30

    # print(images)
    # print(type(images[0]))
    pdfname = content_id + ".pdf"
    with open(pdfname, "wb+") as f:
        f.write(img2pdf.convert(images))
        f = File(f)
        notes = models.Notes.objects.create(notes_id=content_id, title="hello", pdf=f)
        notes.save()

    try:
        shutil.rmtree(os.getcwd() + "/" + str(content_id))
    except:
        pass
    try:
        filename = str(content_id) + ".pdf"
        os.remove(filename)
    except:
        pass
    return render(request, "home.html")
