import datetime

from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm
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


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'index.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def parking_list(request):
    filter_busy = request.GET.get('busy')
    filter_min_price = request.GET.get('min_price')
    filter_max_price = request.GET.get('max_price')

    parkings = ParkingSpot.objects.all()

    if filter_busy == 'busy':
        parkings = parkings.filter(is_busy=True)
    elif filter_busy == 'free':
        parkings = parkings.filter(is_busy=False)

    if filter_min_price:
        parkings = parkings.filter(price__gte=float(filter_min_price))
    if filter_max_price:
        parkings = parkings.filter(price__lte=float(filter_max_price))

    parkings_count = parkings.count()

    return render(
        request,
        'myparking/parking_list.html',
        context={'parkings': parkings, 'parkings_count': parkings_count, },
    )


def rent_parking(request, id):
    parking = get_object_or_404(ParkingSpot, id=id)
    user = request.user

    if request.method == 'POST':
        # Присвоение парковочного места пользователю
        user.parkings.add(parking)
        payment = Payment(owner=user, amount=parking.price, date=datetime.date.today())
        payment.save()
        user.payments.add(payment)

        parking.is_busy = True
        parking.save()
        return redirect('parking_list')  # Перенаправление на список парковочных мест

    return render(
        request,
        'myparking/rent_parking.html',
        context={'parking': parking, },
    )


def my_parking_list(request):
    user = request.user
    parkings = user.parkings.all()
    parkings_count = parkings.count()

    return render(
        request,
        'myparking/my_parking_list.html',
        context={'parkings': parkings, 'parkings_count': parkings_count, },
    )


def my_cars(request):
    user = request.user
    cars = user.cars.all()
    cars_count = cars.count()

    return render(
        request,
        'myparking/my_cars.html',
        context={'cars': cars, 'cars_count': cars_count, },
    )