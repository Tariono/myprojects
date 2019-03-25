import requests
from django.shortcuts import render

# Create your views here.


def show_weather(request):
    cityname = request.GET.get('search')
    APIKEY = '' #Your API key for OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&units=metric&APPID={APIKEY}'
    r = requests.get(url).json()
    if r['cod'] != 200:
        city_weather ={'city':cityname,'cod':r['cod'],}
        context = {'city_weather':city_weather,}
        return render(request, 'index.html', context)
    city_weather = {'city': cityname,
                    'temp': r['main']['temp'],
                    'desc': r['weather'][0]['description'],
                    'pic': r['weather'][0]['icon'],
                    'cod': r['cod'],}
    context = {
                'city_weather':city_weather,
    }
    return render(request, 'index.html', context)
