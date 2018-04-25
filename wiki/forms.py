from django import forms
from .models import Wiki

class WikiForm(forms.ModelForm): # make a form based on the EditWiki model based on the 3 fields below. 
    """form to create bookmarks"""

    # Meta class configures form.ModelForm
    class Meta: # overwriting meta info from modelform 
        model = Wiki
        fields = ('title', 'content', 'author')