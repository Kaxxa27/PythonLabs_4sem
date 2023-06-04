from django.contrib import admin

from .models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('owner', 'mark', 'model', 'license_plate', )


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('number', 'price', 'is_busy')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'park', 'amount', 'receipt_date', 'is_paid', 'repayment_date')
    list_filter = ('receipt_date', 'is_paid', 'repayment_date', 'amount')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount')
    list_filter = ('amount', 'client')
