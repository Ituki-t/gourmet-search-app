from django.shortcuts import render
from django.shortcuts import redirect

from .hotpepper import restaurants_list

# Create your views here.

def index(request):
    restaurants = restaurants_list()
    context = {
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)


def detail(request, restaurant_id):
    for restaurant in restaurants_list():
        if restaurant['id'] == restaurant_id:
            context = {
                'restaurant': restaurant,
            }
            return render(request, 'restaurants/detail.html', context)
    return redirect('index') # 後で404エラーにする
