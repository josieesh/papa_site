from django.http import HttpResponse
from app.models import Textfile
from django.shortcuts import render

HOMEPAGE_NAME = 'Home'
HISTORY_PAGE_NAME= 'History'


def home(request):
    result = Textfile.objects.filter(page=HOMEPAGE_NAME).latest('date_added')
    context = {
        'title': result.name,
        'body': result.text,
    }
    return render(request, 'home.html', context=context)


def history(request):
    result = Textfile.objects.filter(page=HISTORY_PAGE_NAME).latest('id')
    context = {
        'title': result.name,
        'body': result.text
    }

    return render(request, 'history.html', context=context)