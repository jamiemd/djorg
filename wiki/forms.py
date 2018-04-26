from django import forms
from .models import Wiki

class WikiForm(forms.ModelForm):  

    class Meta: 
        model = Wiki
        fields = ('title', 'author', 'content')
