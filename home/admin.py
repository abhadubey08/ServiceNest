from django.contrib import admin
from .models import Category, Service, ElectricianService, ApplianceService, PlumberService, CarpenterService, PainterService, CleaningService, SalonService, MainService, Booking

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)

@admin.register(ElectricianService)
class ElectricianServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(ApplianceService)
class ApplianceServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)

@admin.register(PlumberService)
class PlumberServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(CarpenterService)
class CarpenterServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(PainterService)
class PainterServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(CleaningService)
class CleaningServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(SalonService)
class SalonServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'price')
    list_filter = ('gender',)

@admin.register(MainService)
class MainServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_name')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_number', 'name', 'service', 'email', 'phone', 'created_at')
    search_fields = ('booking_number', 'name', 'email', 'phone')
    list_filter = ('service', 'created_at')
