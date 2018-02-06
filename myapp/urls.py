"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from myapp import views, api

urlpatterns = [
    #path('admin/pages/3', )
    path('admin/', admin.site.urls),
    path('first', views.first, name='first'),
    path('vote', views.vote, name='vote'),
    path('second', views.second, name='second'),
    path('', views.index, name='index'),
    path('results', views.results, name='results'),
    path('third', views.third, name='third'),
    path('fourth', views.fourth, name='fourth'),

    # API
    path('api/results', api.results, name='api_results'),
    path('api/quest1', api.quest1, name='api_quest1'),
    path('api/quest2', api.quest2, name='api_quest2'),
    path('api/quest3', api.quest3, name='api_quest3'),
    path('api/quest4', api.quest4, name='api_quest4'),
]
