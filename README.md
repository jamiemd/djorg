# djorg
Django project with personal organization tools

login:
admin
admin@admin.com
djorg123

# Bookmarks (all in context of bookmarks app)
1. Made model and set up fields for our model (models.py)
2. Made a view that queries the model and renders the template from data in the model (view.py)
3. Made a template that shows the data (index.html)
4. Made a url that matches a path to the view. (url.py)

djorg - refers to overall project
djorg/djorg/urls.py - inner djorg folder refers to the settings for this project


# Migrations



# Commands:
- ./manage.py shell: django and python shell automatically has all django stuff available to it, like import models to database, django stuff
- from bookmarks.model import Bookmark: import bookmark model 
- dir(Bookmark): view object
- Bookmarks.objects.all(): query set to return all bookmarks
- len(Bookmark.object.count(): return count of all bookmarks
- dir(Bookmark.objects): view 

# Make a bookmark in the terminal
1. ./manage.py shell
2. from bookmark.models import Bookmark
3. bookmark = Bookmark(name="Lambda School", url="https://lambdaschool.com") - instantiate
4. bookmark.save() - can view using Bookmarks.objects.all(), returns <QuerySet> which is an iterable, so not quite a python list but almost like it

