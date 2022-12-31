from django.http import HttpResponse
from django.core.paginator import Paginator
from app.models import Page, Chapter
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, View
from app.helpers.contents import sortContents
from typing import List


# HOMEPAGE_NAME = 'Home'
# HISTORY_PAGE_NAME= 'History'
# ENG_FOOT_PAGE_NAME= 'English_Football'

CHAPTERS_PER_PAGE = 1


def landing(request) -> HttpResponse:
    all_pages: List[Page] = list(Page.objects.all())
    
    # If there are no pages, return the default homepage
    if not all_pages:
        return render(request, 'home.html')
    
    page = all_pages[0]
    chapters = Chapter.objects.filter(parent=page).order_by('order')
    chapter = chapters[0]
    response = redirect(f'/{page.url_name}/{chapter.url_name}')
    return response

def view_by_chapter(request, page_name: str = "", chapter_name: str = "") -> HttpResponse:
    page = Page.objects.get(url_name=page_name)
    chapters = Chapter.objects.filter(
                parent=page).order_by("order")
    chapter = chapters.get(url_name=chapter_name)

    paginator = Paginator(chapters, 1)
    chapter_number = chapter.order
    page_obj = paginator.get_page(chapter_number)

    context = {
                'page_name': page.name,
                'chapter': chapter,
                'all_chapters': chapters,
                'paginated_chapters': page_obj,
            }
    return render(request, 'chapter.html', context=context)

  
def view_by_page_name(request, page_name: str = "") -> HttpResponse:
    all_pages: List[Page] = list(Page.objects.all())
    # If there are no pages, return the default homepage
    if not all_pages:
        return render(request, 'home.html')

    for page in all_pages:
        if page.url_name == page_name:
            chapters = Chapter.objects.filter(
                parent=page).order_by('order')

            paginator = Paginator(chapters, CHAPTERS_PER_PAGE)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
	
            context = {
                'page_name': page.name,
                # 'html': html,
                'all_chapters': chapters,
                'paginated_chapters': page_obj,
                'all_pages': all_pages,
                'chapters_per_page': CHAPTERS_PER_PAGE,
            }
            # return render(request=request, template_name="main/movies.html", context={'movies':page_obj})
            return render(request, 'page.html', context=context)

    # By default try to return the first page in the list
    #html = build_page_html(all_pages[0])
    context = {
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