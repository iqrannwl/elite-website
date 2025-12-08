from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User, Campus


class Vehicle(models.Model):
    """Vehicle Management"""
    
    class VehicleType(models.TextChoices):
        BUS = 'BUS', _('Bus')
        VAN = 'VAN', _('Van')
        CAR = 'CAR', _('Car')
    
    vehicle_number = models.CharField(max_length=50, unique=True)
    vehicle_type = models.CharField(
        max_length=10,
        choices=VehicleType.choices,
        default=VehicleType.BUS
    )
    model = models.CharField(max_length=100)
    manufacture_year = models.IntegerField()
    capacity = models.IntegerField()
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='vehicles'
    )
    driver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_vehicle',
        limit_choices_to={'role': 'DRIVER'}
    )
    insurance_number = models.CharField(max_length=100, blank=True, null=True)
    insurance_expiry = models.DateField(blank=True, null=True)
    fitness_certificate_expiry = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'vehicles'
        verbose_name = _('Vehicle')
        verbose_name_plural = _('Vehicles')
    
    def __str__(self):
        return f"{self.vehicle_number} ({self.vehicle_type})"


class Route(models.Model):
    """Transport Route Management"""
    name = models.CharField(max_length=200)
    route_number = models.CharField(max_length=50, unique=True)
    campus = models.ForeignKey(
        Campus,
        on_delete=models.CASCADE,
        related_name='routes'
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='routes'
    )
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    distance_km = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'routes'
        verbose_name = _('Route')
        verbose_name_plural = _('Routes')
    
    def __str__(self):
        return f"{self.route_number} - {self.name}"


class RouteStop(models.Model):
    """Route Stops Management"""
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name='stops'
    )
    stop_name = models.CharField(max_length=200)
    stop_order = models.IntegerField()
    pickup_time = models.TimeField()
    drop_time = models.TimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    class Meta:
        db_table = 'route_stops'
        verbose_name = _('Route Stop')
        verbose_name_plural = _('Route Stops')
        ordering = ['route', 'stop_order']
        unique_together = ['route', 'stop_order']
    
    def __str__(self):
        return f"{self.route.route_number} - {self.stop_name}"


class VehicleMaintenance(models.Model):
    """Vehicle Maintenance Records"""
    
    class MaintenanceType(models.TextChoices):
        ROUTINE = 'ROUTINE', _('Routine Service')
        REPAIR = 'REPAIR', _('Repair')
        ACCIDENT = 'ACCIDENT', _('Accident Repair')
    
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='maintenance_records'
    )
    maintenance_type = models.CharField(
        max_length=20,
        choices=MaintenanceType.choices
    )
    date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    service_center = models.CharField(max_length=200, blank=True, null=True)
    next_service_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_maintenance_records'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'vehicle_maintenance'
        verbose_name = _('Vehicle Maintenance')
        verbose_name_plural = _('Vehicle Maintenance Records')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.vehicle.vehicle_number} - {self.date}"
