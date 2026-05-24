import requests
import os
from dotenv import load_dotenv
from pprint import pprint

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
    results_available = datas['results']['results_available']
    print(results_available)
    # print(datas)
    # pprint(params)

    restaurants = []
    for data in datas['results']['shop']:
        restaurant = {
            'id': data['id'],
            'name': data['name'],
            'url': data['urls']['pc'],
            'access': data['access'],
            'address': data['address'],
            'genre': data['genre']['name'],
            'budget': data['budget']['name'],
            'photo': data['photo']['pc']['l'],
            'open': data['open'],
            'close': data['close'],
            'lat': data['lat'],
            'lng': data['lng'],
            # 'range': data['range'],
        }
        restaurants.append(restaurant)
    return restaurants, datas['results']['results_available']
# pprint(restaurants_list())

def restaurant_detail(restaurant_id):
    params = {
        'key': api_key,
        'format': 'json',
        'id': restaurant_id,
    }
    res = requests.get(api_url, params=params)
    datas = res.json()

    restaurant = {
        'id': datas['results']['shop'][0]['id'],
        'name': datas['results']['shop'][0]['name'],
        'url': datas['results']['shop'][0]['urls']['pc'],
        'access': datas['results']['shop'][0]['access'],
        'address': datas['results']['shop'][0]['address'],
        'genre': datas['results']['shop'][0]['genre']['name'],
        'budget': datas['results']['shop'][0]['budget']['name'],
        'photo': datas['results']['shop'][0]['photo']['pc']['l'],
        'open': datas['results']['shop'][0]['open'],
        'close': datas['results']['shop'][0]['close'],
        'lat': datas['results']['shop'][0]['lat'],
        'lng': datas['results']['shop'][0]['lng'],
    }
    return restaurant


def get_genre_list():
    params = {
        'key': api_key,
        'format': 'json',
    }
    res = requests.get(genre_url, params=params)
    datas = res.json()

    genres = []
    for data in datas['results']['genre']:
        genre = {
            'code': data['code'],
            'name': data['name'],
        }
        genres.append(genre)
    return genres
print(get_genre_list())

def get_budget_list():
    params = {
        'key': api_key,
        'format': 'json',
    }
    res = requests.get(budget_url, params=params)
    datas = res.json()

    budgets = []
    for data in datas['results']['budget']:
        budget = {
            'code': data['code'],
            'name': data['name'],
        }
        budgets.append(budget)
    return budgets
print(get_budget_list())