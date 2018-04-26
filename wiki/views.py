from django.contrib import messages
from django.shortcuts import render
from .forms import WikiForm 
from .models import Wiki 

def wiki_base(request): 
    return render(request, 'wiki_base.html') 


def list(request):  
    context = {'wikis': Wiki.objects.all()} 
    return render(request, 'list.html', context) 


def page(request, id):  
    context = {'wiki_id': Wiki.objects.get(id=id)} 
    print('id', id)
    return render(request, 'page.html', context) 


def add(request): 
    if request.method == 'POST': 
        form = WikiForm(request.POST) 
        if form.is_valid(): 
            form.save() 

    context = {'add': WikiForm()} 
    return render(request, 'add.html', context) 
