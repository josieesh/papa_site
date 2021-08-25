from django.http import HttpResponse
from app.models import Textfile, Page
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, View
from app.helpers.contents import sortContents
from typing import List

# HOMEPAGE_NAME = 'Home'
# HISTORY_PAGE_NAME= 'History'
# ENG_FOOT_PAGE_NAME= 'English_Football'

all_pages: List[Page] = list(Page.objects.all())

def view_by_page_name(request, page_name):
    # If there are no pages, return the default homepage
    if not all_pages:
        return render(request, 'home.html', context={
            'title': 'Placeholder Title',
            'body': 'Placeholder body blah blah blah',
            })

    for page in all_pages:
        if page.name.replace(" ", "_") == page_name:
            context = {
                'page': page
            }
            return render(request, 'page.html', context=context)

    # By default try to return the first page in the list
    context = {
        'page': all_pages[0]
    }
    return render(request, 'page.html', context=context)   
    



# def home(request):
#     result = Textfile.objects.filter(page=HOMEPAGE_NAME).latest('date_added')
#     context = {
#         'title': result.name,
#         'body': result.text,
#     }
#     return render(request, 'home.html', context=context)


# def history(request):
#     results = Textfile.objects.filter(page=HISTORY_PAGE_NAME).order_by('heading_level', 'order')
#     context = sortContents(results)

#     return render(request, 'history.html', context=context)

# def engFoot(request):
#     results = Textfile.objects.filter(page=ENG_FOOT_PAGE_NAME).order_by('heading_level', 'order')
#     context = sortContents(results)

#     return render(request, 'engFoot.html', context=context)