import requests
import pprint 
import os

def get_weather(city):
    """
    Get weather by City
    """
    token = os.getenv("weatherToken")
    token2 = os.environ["secrtet_key"]
    print(token2)
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?appid={token}&q={city}")
    # data = req.json()

    # name = data['name']
    # temp = data['main']['temp']
    # pprint.pprint([name, temp])


if __name__ == "__main__":    
    get_weather("bishkek")