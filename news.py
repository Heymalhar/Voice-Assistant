import requests

from api import *

api_adr = "http://newsapi.org/v2/top-headlines?country=us&apikey=" + key

json_data = requests.get(api_adr).json()

ar = []
i = 0

def news():
    for i in range(3):
        ar.append("Number " + str(i+1) + ": " +json_data["articles"][i]["title"] + " .")
    
    return ar
    
arr = news()
# print(arr)