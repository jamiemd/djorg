from django.shortcuts import render
from .forms import BookmarkForm # import bookmark form
from .models import Bookmark # import model bookmark


#view that takes a request to view a page for the web browser and return a render based on it
def index(request): 
    if request.method == 'POST': # check if post request
        form = BookmarkForm(request.POST) # make BookmarkForm object based on request parameters that user filled in
        if form.is_valid(): # django validation to check if data entered is valid
            form.save() # if valid then save it
    # query all objects by using model class and put them in a dictionary with key 'bookmarks'
    context = {'bookmarks': Bookmark.objects.all(), 
            'form': BookmarkForm()} # make instance of BookmarkForm and pass the instance as a form to the context and now the template will know about the form too
    return render(request, 'bookmarks/index.html', context) # render the request

