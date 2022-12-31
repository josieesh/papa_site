"""papa_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from app import views


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='page'),
    path('<str:page_name>/', views.view_by_page_name, name='page'),
    path('<str:page_name>/<str:chapter_name>', views.view_by_chapter, name='chapter'),
]
# urlpatterns = [
#     path('', RedirectView.as_view(url='english_football', permanent=False), name='home'),
#     path('history/', views.history, name='history'),
#     path('english_football/', views.engFoot, name='eng_foot'),
#     path('admin/', admin.site.urls),
# ]
