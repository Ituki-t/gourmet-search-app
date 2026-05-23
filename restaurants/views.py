from django.shortcuts import render
from django.shortcuts import redirect

from .hotpepper import restaurants_list
from .hotpepper import restaurant_detail

from pprint import pprint

# Create your views here.

def index(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    range = request.GET.get('range')
    # keyword = request.GET.get('keyword')

    restaurants = restaurants_list(lat=lat, lng=lng, range=range)
    pprint(restaurants)
    context = {
        'restaurants': restaurants,
        'lat': lat,
        'lng': lng,
        'range': range,
    }
    return render(request, 'restaurants/index.html', context)


def detail(request, restaurant_id):
    restaurant = restaurant_detail(restaurant_id)

    if not restaurant:
        return render(request, 'restaurants/not_found.html')

    context = {
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/detail.html', context)