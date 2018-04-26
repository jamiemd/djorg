from django import forms
from .models import Wiki, EditWiki

class WikiForm(forms.ModelForm):  

    class Meta: 
        model = Wiki
        fields = ('title', 'author', 'content')

class EditForm(forms.ModelForm):  

    class Meta: 
        model = EditWiki
        fields = ('title', 'author', 'content')