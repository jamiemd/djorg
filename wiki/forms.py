from django import forms
from .models import Add

class WikiForm(forms.ModelForm):  

    class Meta: 
        model = Add
        fields = ('title', 'content')
