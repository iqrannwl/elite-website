from django.contrib import admin
from .models import Vehicle, Route, RouteStop, VehicleMaintenance


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle_number', 'vehicle_type', 'model', 'capacity',
        'campus', 'driver', 'is_active'
    )
    list_filter = ('vehicle_type', 'campus', 'is_active')
    search_fields = ('vehicle_number', 'model')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'route_number', 'name', 'campus', 'vehicle',
        'start_location', 'end_location', 'monthly_fee', 'is_active'
    )
    list_filter = ('campus', 'is_active')
    search_fields = ('route_number', 'name')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(RouteStop)
class RouteStopAdmin(admin.ModelAdmin):
    list_display = ('route', 'stop_name', 'stop_order', 'pickup_time', 'drop_time')
    list_filter = ('route',)
    search_fields = ('stop_name',)
    ordering = ['route', 'stop_order']


@admin.register(VehicleMaintenance)
class VehicleMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'maintenance_type', 'date', 'cost', 'next_service_date')
    list_filter = ('maintenance_type', 'date')
    search_fields = ('vehicle__vehicle_number', 'service_center')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')
