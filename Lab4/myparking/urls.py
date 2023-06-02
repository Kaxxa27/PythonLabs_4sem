from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
     path('register/', views.registration_view, name='register'),
    # path('cars/', views.car_list, name='car_list'),  # URL-шаблон для списка автомобилей
    # path('cars/<int:pk>/', views.car_detail, name='car_detail'),  # URL-шаблон для деталей автомобиля
]
