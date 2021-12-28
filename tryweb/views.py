from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
from .models import City
from .forms import CityForm

# Create your views here.


# def frame(request):
#     return HttpResponse("конфигуратор")


def index(request):
    appid = '09910f9f5d636c845af090615c1934b8'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()  # очищаем форму

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'tryweb/index.html', context)


def about(request):
    return render(request, 'tryweb/about.html')


def biss(request):
    return render(request, 'tryweb/biss.html')


def frame(request):
    return render(request, 'tryweb/frame.html')
