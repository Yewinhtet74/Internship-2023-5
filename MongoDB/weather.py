import json
import requests
key = '8a6d6b7f7fe81a7b09ebbfa266296ce2'
url='http://api.openweathermap.org/data/2.5/weather?appid=8a6d6b7f7fe81a7b09ebbfa266296ce2&q='
cityName=input('Please enter your city name')
newUrl=url+cityName
jsonData = requests.get(newUrl).json()
print(type(jsonData))
print(jsonData)