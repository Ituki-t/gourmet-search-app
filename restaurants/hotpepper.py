import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('HOTPEPPER_API_KEY')
api_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
genre_url = "http://webservice.recruit.co.jp/hotpepper/genre/v1/"
budget_url = "http://webservice.recruit.co.jp/hotpepper/budget/v1/"

def restaurants_list(lat=None, lng=None, range=3, start=1, keyword=None, genre=None, budget=None):
    params = {
        'key': api_key,
        'format': 'json',
        'count': 10,
        'start': start,
        'keyword': keyword,
        'genre': genre,
        'budget': budget,
    }

    if lat not in [None, '', 'None'] and lng not in [None, '', 'None']:
        params['lat'] = lat
        params['lng'] = lng
        params['range'] = range
    else:
        params['large_area'] = 'Z011' # 東京

    res = requests.get(api_url, params=params)
    datas = res.json()

    results = datas.get('results', {})
    shops = results.get('shop', [])
    results_available = results.get('results_available', 0)

    restaurants = []

    for data in shops:
        restaurant = {
            "id": data.get("id"),
            "name": data.get("name"),
            "url": data.get("urls", {}).get("pc"),
            "access": data.get("access"),
            "address": data.get("address"),
            "genre": data.get("genre", {}).get("name"),
            "budget": data.get("budget", {}).get("name"),
            "photo": data.get("photo", {}).get("pc", {}).get("l"),
            "open": data.get("open"),
            "close": data.get("close"),
            "lat": data.get("lat"),
            "lng": data.get("lng"),
        }
        restaurants.append(restaurant)
    return restaurants, results_available

def restaurant_detail(restaurant_id):
    params = {
        'key': api_key,
        'format': 'json',
        'id': restaurant_id,
    }
    res = requests.get(api_url, params=params)
    datas = res.json()

    results = datas.get('results', {})
    shops = results.get('shop', [])

    if not shops:
        return None

    data = shops[0]

    restaurant = {
        "id": data.get("id"),
        "name": data.get("name"),
        "url": data.get("urls", {}).get("pc"),
        "access": data.get("access"),
        "address": data.get("address"),
        "genre": data.get("genre", {}).get("name"),
        "budget": data.get("budget", {}).get("name"),
        "photo": data.get("photo", {}).get("pc", {}).get("l"),
        "open": data.get("open"),
        "close": data.get("close"),
        "lat": data.get("lat"),
        "lng": data.get("lng"),
    }
    return restaurant


def get_genre_list():
    params = {
        'key': api_key,
        'format': 'json',
    }
    res = requests.get(genre_url, params=params)
    datas = res.json()

    results = datas.get('results', {})
    genre_datas = results.get('genre', [])

    genres = []
    for data in genre_datas:
        genre = {
            'code': data.get('code'),
            'name': data.get('name'),
        }
        genres.append(genre)
    return genres

def get_budget_list():
    params = {
        'key': api_key,
        'format': 'json',
    }
    res = requests.get(budget_url, params=params)
    datas = res.json()

    results = datas.get('results', {})
    budget_datas = results.get('budget', [])

    budgets = []
    for data in budget_datas:
        budget = {
            'code': data['code'],
            'name': data['name'],
        }
        budgets.append(budget)
    return budgets