from django import forms
from .models import Edit

class WikiForm(forms.ModelForm):  
    """form to create bookmarks"""

    # Meta class configures form.ModelForm
    class Meta: # overwriting meta info from modelform 
        model = Edit
        fields = ('title', 'content',)