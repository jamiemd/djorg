from django.shortcuts import render
from .forms import BookmarkForm # import bookmark form
from .models import Bookmark # import model bookmark


#view that takes a request to view a page for the web browser and return a render based on it
def index(request): # define view method that takes a request
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
    # query all objects by using model class and put them in a dictionary with key 'bookmarks'
    context = {'bookmarks': Bookmark.objects.all(), 
            'form': BookmarkForm()}   
    return render(request, 'bookmarks/index.html', context) # render the request

