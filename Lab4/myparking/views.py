from django.shortcuts import render
from .models import *

def index(request):
    """
       Функция отображения для домашней страницы сайта.
    """
    parkings = ParkingSpot.objects.all()
    parkings_count = ParkingSpot.objects.all().count()

    return render(
        request,
        'index.html',
        context={'parkings': parkings, 'parkings_count': parkings_count, },
    )
