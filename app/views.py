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


def view_by_page_name(request, page_name: str) -> HttpResponse:
    # If there are no pages, return the default homepage
    if not all_pages:
        return render(request, 'home.html', context={
            'title': 'Placeholder Title',
            'body': 'Placeholder body blah blah blah',
            })

    for page in all_pages:
        if page.url_name == page_name:
            # html = build_page_html(page)
            context = {
                'page_name': page.name,
                # 'html': html,
                'page': page,
                'all_pages': all_pages
            }

            return render(request, 'page.html', context=context)

    # By default try to return the first page in the list
    #html = build_page_html(all_pages[0])
    context = {
        'page_name': all_pages[0].name,
        #'html': html,
        'page': all_pages[0],
        'all_pages': all_pages
    }
    return render(request, 'page.html', context=context)   
    
    


def build_page_html(page: Page) -> str:
    html = """
    <div class="content_container">
    {% include "toc.html" %}
    """
    contents = dict()
    for chapter in page.children.all(): # Good news: django only fetches lazily meaning a page's children are only fetched when that field is accessed
        html += f"<h1 id={chapter.id}>{chapter.name}</h1>"
        html += chapter.text

        for heading in chapter.children.all():
            html += f"<h2 id={heading.id}>{heading.name}</h2>"
            html += heading.text

            for level2heading in heading.children.all():
                html+= f"<h3 id={level2heading.id}>{level2heading.name}</h3>"
                html += level2heading.text

                for level3heading in level2heading.children.all():
                    html += f"<h4 id={level3heading.id}>{level3heading.name}</h4>"
                    html += level3heading.text

                    for level4heading in level3heading.children.all():
                        html += f"<h5 id={level4heading.id}>{level4heading.name}</h5>"
                        html += level4heading.text

    html += "</div>"
    return html
    



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