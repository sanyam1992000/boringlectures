from time import sleep
import shutil
import os
import img2pdf
# from background_task import background
from django.core.files import File
from urllib.request import urlopen
import requests
import json
from . import models
from .models import Notes
from celery import shared_task

@shared_task()
def sleepy():
    notes = Notes.objects.get_or_create(title="testing", notes_id=12)
    sleep(10)
    return None

@shared_task()
def get_notes(content_id):
    notes = models.Notes.objects.get(notes_id=content_id)
    content_id = str(content_id)
    base_url = "https://lecturenotes.in/material/" + str(content_id)
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
        print("Creation of the directory  failed", OSError)
    next_page = True

    images = []
    total_pages = 0
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
                total_pages += 1
                notes.total_pages += 1
                notes.save()

        page_no += 30


    with open("{}.pdf".format(content_id), "wb") as f:
        f.write(img2pdf.convert(images))
    pdf = open("{}.pdf".format(content_id), "rb+")
    p1 = File(pdf)
    notes.pdf = p1
    notes.title = "done"
    notes.save()
    # notes.delete()
    # notes = models.Notes.objects.create(notes_id=content_id, title="done scrapping", pdf=p1, total_pages=total_pages)

    shutil.rmtree(os.getcwd() + "/" + str(content_id))
    return None

@shared_task()
def get_pdf(content_id):
    notes = models.Notes.objects.get(notes_id=content_id)
    content_id = str(content_id)
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

    next_page = True
    total_pages = 0
    images = []
    while (next_page):
        url = "https://lecturenotes.in/material/" + str(content_id) + "/page-" + str(page_no) + "?noOfItems=30"

        data = client.get(url, headers=head)
        # print(data.content)
        d = json.loads(data.text)
        if (len(d['page']) < 30):
            next_page = False

        img_base_url = "https://lecturenotes.in"
        flag = 0
        for pg in d['page']:
            # print(pg['path'])
            r = client.get(img_base_url + pg['path'], headers=head)
            # print(r.url)
            from PIL import Image

            if flag != 0:
                img = Image.open(urlopen(r.url))
                im1 = img.convert('RGB')
                images.append(img)
                total_pages += 1
                notes.total_pages += 1
                notes.save()
            else:
                img1 = Image.open(urlopen(r.url))
                image1 = img1.convert('RGB')
                total_pages += 1
                flag += 1
                notes.total_pages += 1
                notes.save()
            sleep(2)
        page_no += 30

    image1.save(r'{}.pdf'.format(content_id), save_all=True, append_images=images)
    notes.delete()
    pdf = open('{}.pdf'.format(content_id), "rb+")
    p1 = File(pdf)
    notes = models.Notes.objects.create(notes_id=content_id, title="done scrapping", pdf=p1, total_pages=total_pages)
    return
