from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    city = request.GET.get("city", "London")
    api_key = "c7a2c0d5fb86e2f2cc1075204bb3aa5a"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    context = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
    }
    return render(request, "weather/weather.html", context)
