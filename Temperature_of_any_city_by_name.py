

# Python program to get Temperature of any city by name


import requests

api_address = 'http://api.openweathermap.org/data/2.5/wether?'
#API Key
api_address += 'appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input('City Name : ')
url = api_address + city
json_data = requests.get(url).json()
temp = str(json_data['main']['temp'] - 273.15)
print(temp + " degrees")
# ============== OUTPUT ==============
# City Name : california
# 20.0 degrees



