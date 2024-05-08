import requests
from api import *

api_adr = 'http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=' + key2

json_data = requests.get(api_adr).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273, 1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

# print(temp())
# print(des())