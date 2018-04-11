from django.shortcuts import render
from .models import Bookmark # import model bookmark

#view that takes a request to view a page for the web browser and return a render based on it
def index(request): # define view method that takes a request
    context = {'bookmarks': Bookmark.objects.all()} # query all objects by using model class and put them in a dictionary with key 'bookmarks'
    return render(request, 'bookmarks/index.html', context) # render the request

    