from django import forms
from .models import Wiki, EditForm

class WikiForm(forms.ModelForm):  

    class Meta: 
        model = Wiki
        fields = ('title', 'content')


class EditForm(forms.ModelForm):  

    class Meta: 
        model = EditForm
        fields = ('title', 'content')

