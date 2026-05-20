import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
api_key = os.getenv('HOTPEPPER_API_KEY')
api_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"

def restaurants_list():
    params = {
        'key': api_key,
        'format': 'json',
        'count': 50, # ここは後から件数を指定できるようにしよう
        'keyword': '東京',
    }
    res = requests.get(api_url, params=params)
    datas = res.json()
    # print(datas)

    restaurants = []
    for data in datas['results']['shop']:
        restaurant = {
            'name': data['name'],
            'access': data['access'],
            'address': data['address'],
            'genre': data['genre']['name'],
            'budget': data['budget']['name'],
            'photo': data['photo']['pc']['l'],
        }
        restaurants.append(restaurant)
    return restaurants
pprint(restaurants_list())