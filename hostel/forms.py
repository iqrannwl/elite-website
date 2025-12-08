from django import forms
from hostel.models import Hostel, Room


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ['name', 'hostel_type', 'address', 'warden_name', 'warden_phone', 
                  'total_rooms', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'warden_name': forms.TextInput(attrs={'class': 'form-control'}),
            'warden_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'total_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                if isinstance(field.widget, forms.CheckboxInput):
                    field.widget.attrs['class'] = 'form-check-input'
                elif isinstance(field.widget, forms.Select):
                    field.widget.attrs['class'] = 'form-select'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['hostel', 'room_number', 'room_type', 'capacity', 'current_occupancy']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_occupancy': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                if isinstance(field.widget, forms.Select):
                    field.widget.attrs['class'] = 'form-select'
