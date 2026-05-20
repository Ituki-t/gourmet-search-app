from django.shortcuts import render

from .hotpepper import restaurants_list

# Create your views here.

def index(request):
    restaurants = restaurants_list()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)
