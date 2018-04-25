from django.urls import path # path built in that matches url patterns

from . import views # import views from current directory (views.py file)

urlpatterns = [ # define list that matches and adds to views
    path('', views.wiki_base),
    path('list', views.list),
    path('add', views.add_wiki),
    # path('edit', views.edit_wiki),
   
]