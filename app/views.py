from django.http import HttpResponse
from app.models import Textfile
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, View
from app.helpers.contents import sortContents

HOMEPAGE_NAME = 'Home'
HISTORY_PAGE_NAME= 'History'
ENG_FOOT_PAGE_NAME= 'English_Football'



def home(request):
    result = Textfile.objects.filter(page=HOMEPAGE_NAME).latest('date_added')
    context = {
        'title': result.name,
        'body': result.text,
    }
    return render(request, 'home.html', context=context)


def history(request):
    results = Textfile.objects.filter(page=HISTORY_PAGE_NAME).order_by('heading_level', 'order')
    context = sortContents(results)

    return render(request, 'history.html', context=context)

def engFoot(request):
    results = Textfile.objects.filter(page=ENG_FOOT_PAGE_NAME).order_by('heading_level', 'order')
    context = sortContents(results)

    return render(request, 'engFoot.html', context=context)