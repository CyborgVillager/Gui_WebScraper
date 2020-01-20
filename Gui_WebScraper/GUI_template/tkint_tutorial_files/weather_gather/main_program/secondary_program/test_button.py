import requests
from colors import *

def test_function(entry):
    print('Button Clicked',entry)


def get_weather(city):
    weather_key = '3d7102c18ab158257bce2ab1be33d4df'
    #url = 'https://api.openweathermap.org/data/2.5/forecast'
    # weather = current
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key,'q':city,'units':'imperial'}
    response = requests.get(url,params=params)
    weather_response = response.json()
  # print(response.json())
    print('You\'ve searched for: ' , weather_response['name'])
    # get the first entry & the 'description' as listed in the terminal after print(response.json()) was active
    print('It\'s currently' , red , weather_response['weather'][0]['description'], end, ' at this time.')

# Temperature Color change, if its >= 70 -> red , else its blue
    if weather_response['main']['temp'] >= 70:
        print('Temperature: ' ,red , weather_response['main']['temp'],end )
    else:
        print('Temperature: ', blue, weather_response['main']['temp'], end)
# MAX TEMP
    if weather_response['main']['temp_max'] >= 70:
        print('Max Temperature: ' , red, weather_response['main']['temp_max'], end)
    else:
        print('Max Temperature: ', blue, weather_response['main']['temp_max'], end)

    print('Humidity: ' , cyan, weather_response['main']['humidity'], end)
    print('Wind Speed: ' , weather_response['wind']['speed'], ' Mph')