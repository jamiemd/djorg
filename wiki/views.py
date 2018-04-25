from django.shortcuts import render
from .forms import WikiForm 
from .models import Wiki 

def index(request): 
    if request.method == 'POST': 
        form = WikiForm(request.POST) 
        if form.is_valid(): 
            form.save() 
    context = {'wikis': Wiki.objects.all(), 
            'form': WikiForm()} 
    return render(request, 'wikis/index.html', context) 

