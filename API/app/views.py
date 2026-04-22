from django.shortcuts import render
import requests

# Create your views here.
def get_weather(request):
    url='https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&hourly=temperature_2m%22'
    response=requests.get(url)
    data=response.json()

    times=data['hourly']['time']
    temps=data['hourly']['temperature_2m']

    combined_data=[]
    for t,temp in zip(times,temps):
        combined_data.append({
            'time' :t,
            'temperature':temp
            })
        
    return render(request,'weather.html',{'weather_list':combined_data})




from rest_framework.response import response
from rest_framework.decorations import api_view
from .models import product
from .serializers import productserializer



@api_view(['GET'])
def product_list(request):
    products=product.objects.all()
    serializer=productserializer(products,many=True)
    