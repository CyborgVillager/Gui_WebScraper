import requests

def test_function(entry):
    print('Button Clicked',entry)


def get_weather(city):
    weather_key = '3d7102c18ab158257bce2ab1be33d4df'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID':weather_key,'q':city,'units':'imperial'}
    response = requests.get(url,params=params)
    print(response.json())