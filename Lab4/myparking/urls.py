from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
     path('register/', views.registration_view, name='register'),
     path('parking_list/', views.parking_list, name='parking_list'),
     path('my_parking_list/', views.my_parking_list, name='my_parking_list'),
     path('rent_parking/<int:id>/', views.rent_parking, name='rent_parking'),
    # path('cars/', views.car_list, name='car_list'),  # URL-шаблон для списка автомобилей
    # path('cars/<int:pk>/', views.car_detail, name='car_detail'),  # URL-шаблон для деталей автомобиля
]
