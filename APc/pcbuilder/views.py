from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Component
import datetime

def index(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       price = request.POST['price']

       component = Component(title=title)
       component.price = price
       component.save()

    # Get all posts from DB
    components = Component.objects 
    return render_to_response('index.html', {'Components': components},
                              context_instance=RequestContext(request))

