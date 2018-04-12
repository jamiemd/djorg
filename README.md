# djorg
Django project with personal organization tools

# Bookmarks (all in context of bookmarks app)
1. Made model and set up fields for our model (models.py)
2. Made a view that queries the model and renders the template from data in the model (view.py)
3. Made a template that shows the data (index.html)
4. Made a url that matches a path to the view. (url.py)

djorg - refers to overall project
djorg/djorg/urls.py - inner djorg folder refers to the settings for this project

#Make a bookmark
1. ./manage.py shell
2. from bookmark.models import Bookmark
3. bookmark = Bookmark(name="Lambda School", url="https://lambdaschool.com")
4. bookmark.save()