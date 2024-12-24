import os
import requests


api_key= os.getenv("ApiKeyForWeatherApp")


city_name=input("Enter the name of the city you want to find the weather for: ")

url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

data= requests.get(url)

#print(data.status_code)

#print(data.json()['weather'][0]['description'])

print(data.json())
