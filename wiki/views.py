from django.contrib import messages
from django.shortcuts import render
from .forms import WikiForm, EditForm
from .models import Wiki 

def wiki_base(request): 
    return render(request, 'wiki_base.html') 


def list(request):  
    context = {'wikis': Wiki.objects.all()} 
    return render(request, 'list.html', context) 


def page(request, id):  
    context = {'wiki': Wiki.objects.get(id=id)} 
    return render(request, 'page.html', context) 


def add(request): 
    if request.method == 'POST': 
        form = WikiForm(request.POST) 
        if form.is_valid(): 
            form.save() 

    context = {'add': WikiForm()} 
    return render(request, 'add.html', context) 


def edit(request, id): 
    wiki = Wiki.objects.get(id=id)
    if request.method == 'POST': 
        form = EditForm(request.POST, instance=wiki) 
        if form.is_valid(): 
            form.save() 
            return redirect(id)
    context = {'form': EditForm(instance=wiki), 'wiki': wiki} 
    return render(request, 'edit.html', context) 


# def delete(request, id):
#     wiki = Wiki.objects.get(id=id)
#     if request.method == 'POST': 
#         form = EditForm(request.POST, instance=wiki) 
#             form.delete() 
#             return redirect(id)
#     context = {'form': EditForm(instance=wiki), 'wiki': wiki} 
#     return render(request, 'edit.html', context) 