from django import forms
from transport.models import Vehicle, Route, RouteStop


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'model', 'capacity', 
                  'driver_name', 'driver_phone', 'driver_license', 'is_active']
        widgets = {
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'driver_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'driver_license': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                if isinstance(field.widget, forms.CheckboxInput):
                    field.widget.attrs['class'] = 'form-check-input'
                elif isinstance(field.widget, forms.Select):
                    field.widget.attrs['class'] = 'form-select'


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'vehicle', 'start_point', 'end_point', 'distance', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_point': forms.TextInput(attrs={'class': 'form-control'}),
            'end_point': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                if isinstance(field.widget, forms.CheckboxInput):
                    field.widget.attrs['class'] = 'form-check-input'
                elif isinstance(field.widget, forms.Select):
                    field.widget.attrs['class'] = 'form-select'


class RouteStopForm(forms.ModelForm):
    class Meta:
        model = RouteStop
        fields = ['route', 'stop_name', 'stop_order', 'pickup_time', 'drop_time']
        widgets = {
            'stop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'stop_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'pickup_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'drop_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'route' in self.fields:
            self.fields['route'].widget.attrs['class'] = 'form-select'
