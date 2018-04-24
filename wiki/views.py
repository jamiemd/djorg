from django.shortcuts import render
# from .forms import WikiForm 
from .models import Wiki 

def index(request): 
    # if request.method == 'POST': 
    #     form = WikiForm(request.POST) 
    #     if form.is_valid(): 
    #         form.save() 
    # context = {'wiki': Wiki.objects.all(), 
    #         'form': WikiForm()} 
    context = {'wiki': Wiki.objects.all()} 
    return render(request, 'wikis/index.html', context) 

