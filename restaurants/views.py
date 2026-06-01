from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SearchForm
from .hotpepper import restaurants_list
from .hotpepper import restaurant_detail

from pprint import pprint

# Create your views here.

def index(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    range_value = 3 # デフォルトの検索範囲（1000m）
    keyword = '' # デフォルトのキーワード
    genre = None
    budget = None

    form = SearchForm(request.GET)
    if form.is_valid():
        range_value = form.cleaned_data['range']
        keyword = form.cleaned_data['keyword']
        genre = form.cleaned_data['genre']
        budget = form.cleaned_data['budget']

    # ページング
    page = int(request.GET.get('page', 1))
    count = int(request.GET.get('count', 10)) # 1ページあたりの件数
    start = (page - 1) * count + 1

    restaurants, results_available = restaurants_list(lat=lat, lng=lng, range=range_value, start=start, keyword=keyword, genre=genre, budget=budget)

    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if results_available > page * count else None

    context = {
        'restaurants': restaurants,
        'lat': lat,
        'lng': lng,
        'range': range_value,
        'results_available': results_available,
        'page': page,
        'prev_page': prev_page,
        'next_page': next_page,
        'form': form,
        'keyword': keyword,
        'genre': genre,
        'budget': budget,
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