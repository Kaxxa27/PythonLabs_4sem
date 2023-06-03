from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
     path('register/', views.registration_view, name='register'),
     path('parking_list/', views.parking_list, name='parking_list'),
     path('my_parking_list/', views.my_parking_list, name='my_parking_list'),
     path('my_cars/', views.my_cars, name='my_cars'),
     path('add_car/', views.add_car, name='add_car'),
     path('delete_car/<int:id>/', views.delete_car, name='delete_car'),
     path('rent_parking/<int:id>/', views.rent_parking, name='rent_parking'),
     path('add_car_in_park/<int:id>/', views.add_car_in_parkingslot, name='add_car_in_parkingslot'),
     path('add_car_to_parking/<int:car_id>/<int:park_id>', views.add_car_to_parking, name='add_car_to_parking'),
]
