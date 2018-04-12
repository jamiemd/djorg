from django import forms

from .models import Bookmark

class BookmarkForm(forms.ModelForm): # make a form based on the bookmark model based on the 3 fields below. 
    """form to create bookmarks"""

    class Meta: # overwriting meta info from modelform
        model = Bookmark
        fields = ('url', 'name', 'notes')