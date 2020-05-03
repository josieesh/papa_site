from django.http import HttpResponse
from app.models import Textfile
from django.shortcuts import render

HOMEPAGE_NAME = 'Home'


def home(request):
    result = Textfile.objects.filter(page=HOMEPAGE_NAME).latest('date')
    context = {
        'title': result.name,
        'body': result.text,
    }
    print("\n")
    print(context)
    return render(request, 'home.html', context=context)