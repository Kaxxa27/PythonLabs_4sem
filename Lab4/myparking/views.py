from datetime import datetime, timedelta

import requests
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
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
        сurrent_date = datetime.now()
        payment = Payment(owner=user,
                          park=parking,
                          amount=parking.price,
                          receipt_date=сurrent_date,
                          receipt_time=сurrent_date.time())
        payment.save()
        user.payments.add(payment)
        parking.is_busy = True
        parking.date_of_rent = сurrent_date
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


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user  # Установка владельца
            car.save()
            cars = request.user.cars.all()
            return render(request,
                          'myparking/my_cars.html',
                          context={'cars': cars, 'cars_count': cars.count(), }, )
    else:
        form = CarForm()

    return render(request, 'myparking/add_car.html', {'form': form})


def delete_car(request, id):
    try:
        Car.objects.filter(id=id).delete()
    except Exception as e:
        print(f"Удаление не получилось. Код ошибки {str(e)}")
    return redirect('my_cars')


def car_in_park(request, park_id, status):
    parking = get_object_or_404(ParkingSpot, id=park_id)

    if status == 'add':
        user_cars = request.user.cars.all()
        parking_cars = parking.cars.all()
        cars_to_add = user_cars.difference(parking_cars)
    if status == 'del':
        cars_to_add = parking.cars.all()

    return render(
        request,
        'myparking/car_list_for_park.html',
        context={'parking': parking, 'cars': cars_to_add,
                 'cars_count': cars_to_add.count(), 'status': status},
    )


def interaction_car_for_parking(request, car_id, park_id, status):
    car = get_object_or_404(Car, id=car_id)
    parking = get_object_or_404(ParkingSpot, id=park_id)
    try:
        if status == 'add':
            parking.cars.add(car)
        if status == 'del':
            parking.cars.remove(car)
    except Exception as e:
        print(f"Код ошибки {str(e)}")
    return redirect('my_parking_list')


def delete_park(request, park_id):
    parking = get_object_or_404(ParkingSpot, id=park_id)
    user = request.user
    try:
        for payment in user.payments.filter(park_id=park_id):
            if not payment.is_paid:
                return render(request, 'myparking/not_all_payments_paid.html')
        parking.is_busy = False
        parking.save()
        user.parkings.remove(parking)

    except Exception as e:
        print(f"Код ошибки {str(e)}")
    return redirect('my_parking_list')


def my_payments(request):
    user = request.user
    payments = user.payments.all()

    payments = payments.order_by('-id')
    payments_count = payments.count()

    # Создание массива, для вычисления, сколько дней осталось до погашения платежей
    datetimes = [datetime.combine(payment.receipt_date, payment.receipt_time) for payment in payments]
    time_to_repay_the_payment = timedelta(weeks=1)
    # time_to_repay_the_payment = timedelta(seconds=20)
    current_datetime = datetime.now()
    zero_timedelta = timedelta(0)
    datetimes_for_repay_the_payment = [
        dt + time_to_repay_the_payment - current_datetime
        if dt + time_to_repay_the_payment - current_datetime >= zero_timedelta else 0
        for dt in datetimes
    ]

    return render(
        request,
        'myparking/my_payments.html',
        context={'payments': payments,
                 'payments_count': payments_count,
                 'datetimes_for_repay_the_payment': datetimes_for_repay_the_payment},
    )


def payment_paid(request, payment_id):
    user = request.user
    payment = get_object_or_404(Payment, id=payment_id)

    if request.method == 'POST':
        if user.account.amount < payment.amount:
            return render(request, 'myparking/not_enough_money_for_paid.html')

        payment.repayment_date = datetime.now()
        payment.repayment_time = payment.repayment_date.time()
        payment.is_paid = True
        payment.save()

        user.account.amount -= payment.amount
        user.account.save()
        return redirect('my_payments')

    return render(
        request,
        'myparking/payment_paid.html',
        context={'payment': payment, },
    )


def update_payments(request):
    user = request.user
    payments = user.payments.all()
    current_date = datetime.now()
    # time_to_repeat_the_payment = timedelta(weeks=4)
    time_to_repeat_the_payment = timedelta(days=1)
    for park in user.parkings.all():
        print(park.date_of_rent)
        print(time_to_repeat_the_payment)
        print(park.date_of_rent + time_to_repeat_the_payment)

        if park.date_of_rent + time_to_repeat_the_payment <= current_date.date():
            new_payment = Payment(owner=user,
                                  park=park,
                                  amount=park.price,
                                  receipt_date=current_date,
                                  receipt_time=current_date.time())
            new_payment.save()
            user.payments.add(new_payment)
            park.date_of_rent = current_date
            park.save()
    return redirect('my_payments')


def get_ip(request):
    url = f'https://api.ipify.org?format=json'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render(request, 'myparking/get_ip.html',
                      {'ip': data['ip'], })
    else:
        error_message = f"Error: {response.status_code}"
        return render(request, 'myparking/get_ip.html',
                      {'error_message': error_message})


def get_fact_about_cats(request):
    url = f'https://catfact.ninja/fact'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render(request, 'myparking/get_fact_about_cats.html',
                      {'fact': data['fact'], })
    else:
        error_message = f"Error: {response.status_code}"
        return render(request, 'myparking/get_fact_about_cats.html',
                      {'error_message': error_message})
