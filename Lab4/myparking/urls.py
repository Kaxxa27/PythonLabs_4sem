from django.urls import path
from . import views


urlpatterns = [
     path(r'', views.index, name='index'),
     path('register/', views.registration_view, name='register'),

     path('parking_list/', views.parking_list, name='parking_list'),
     path('delete_park/<int:park_id>/', views.delete_park, name='delete_park'),
     path('my_parking_list/', views.my_parking_list, name='my_parking_list'),
     path('rent_parking/<int:id>/', views.rent_parking, name='rent_parking'),

     path('my_cars/', views.my_cars, name='my_cars'),
     path('add_car/', views.add_car, name='add_car'),
     path('delete_car/<int:id>/', views.delete_car, name='delete_car'),

     # Пути для перехода к списку машин на паркинге (status = add/del)
     path('car_in_park/<int:park_id>/<slug:status>/',
          views.car_in_park, name='car_in_park'),

     # Пути для перехода к действиям с авто из паркинга ("На паркинг", "С паркинга")
     path('interaction_car_for_parking/<int:car_id>/<int:park_id>/<slug:status>/',
          views.interaction_car_for_parking, name='interaction_car_for_parking'),

     #  Payments
     path('my_payments/',
          views.my_payments, name='my_payments'),
     path('payment_paid/<int:payment_id>/',
          views.payment_paid, name='payment_paid'),
]
