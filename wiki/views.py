from django.shortcuts import render
from .forms import WikiForm 
from .models import Wiki 

def wiki_base(request): 
    return render(request, 'wiki_base.html') 

def list(request):  
    context = {'wikis': Wiki.objects.all()} 
    return render(request, 'wiki_list.html', context) 


# def add_wiki(request): 
#     if request.method == 'POST': 
#         form = WikiForm(request.POST) 
#         if form.is_valid(): 
#             form.save() 
#     context = {'form': WikiForm()} 
#     return render(request, 'wiki_base.html', context) 


# def edit_wiki(request): 
#     if request.method == 'POST': 
#         form = WikiForm(request.POST) 
#         if form.is_valid(): 
#             form.save() 
#     context = {'wikis': Wiki.objects.all(), 
#             'form': WikiForm()} 
#     return render(request, '.html', context) 

