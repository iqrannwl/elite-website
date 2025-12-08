from django import forms
from staff.models import Staff, Department, Designation, Leave, LeaveType
from accounts.models import User


class StaffForm(forms.ModelForm):
    # User fields
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    gender = forms.ChoiceField(
        choices=[('', 'Select Gender'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        required=False
    )
    phone_number = forms.CharField(max_length=20, required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    
    class Meta:
        model = Staff
        fields = [
            'employee_id', 'department', 'designation', 'campus', 'date_of_joining',
            'employment_type', 'qualification', 'experience_years', 'basic_salary',
            'is_active', 'emergency_contact_name', 'emergency_contact_phone',
            'emergency_contact_relation', 'bank_name', 'account_number', 'account_holder_name'
        ]
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
        
        if self.instance.pk and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['date_of_birth'].initial = self.instance.user.date_of_birth
            self.fields['gender'].initial = self.instance.user.gender
            self.fields['phone_number'].initial = self.instance.user.phone_number
            self.fields['address'].initial = self.instance.user.address
    
    def save(self, commit=True):
        staff = super().save(commit=False)
        
        if staff.user_id:
            user = staff.user
        else:
            username = self.cleaned_data['email'].split('@')[0]
            base_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            
            user = User.objects.create_user(
                username=username,
                email=self.cleaned_data['email'],
                password='staff123',
                role=User.UserRole.TEACHER
            )
        
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.gender = self.cleaned_data.get('gender')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.address = self.cleaned_data.get('address')
        
        if commit:
            user.save()
            staff.user = user
            staff.save()
        
        return staff


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['staff', 'leave_type', 'start_date', 'end_date', 'reason', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                if isinstance(field.widget, forms.Select):
                    field.widget.attrs['class'] = 'form-select'
                else:
                    field.widget.attrs['class'] = 'form-control'
