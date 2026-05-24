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

    # ページング対応
    page = request.GET.get('page', 1)
    count = request.GET.get('count', 10) # 1ページあたりの件数
    start = (int(page) - 1) * count + 1
    prev_page = int(page) - 1 if int(page) > 1 else None
    next_page = int(page) + 1

    restaurants, results_available = restaurants_list(lat=lat, lng=lng, range=range, start=start)
    pprint(restaurants)
    context = {
        'restaurants': restaurants,
        'lat': lat,
        'lng': lng,
        'range': range,
        'results_available': results_available,
        'page': page,
        'prev_page': prev_page,
        'next_page': next_page,
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