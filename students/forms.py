from django import forms
from students.models import Student
from accounts.models import User


class StudentForm(forms.ModelForm):
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
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    postal_code = forms.CharField(max_length=20, required=False)
    
    class Meta:
        model = Student
        fields = [
            'admission_number', 'admission_date', 'campus', 'current_class', 
            'section', 'roll_number', 'blood_group', 'religion', 'caste', 
            'nationality', 'father_name', 'father_phone', 'father_occupation', 
            'father_email', 'mother_name', 'mother_phone', 'mother_occupation', 
            'mother_email', 'guardian_name', 'guardian_phone', 'guardian_relation',
            'guardian_email', 'emergency_contact_name', 'emergency_contact_phone',
            'emergency_contact_relation', 'previous_school', 'previous_class',
            'medical_conditions', 'allergies', 'medications', 'uses_transport',
            'route', 'is_hosteler', 'hostel_room', 'status'
        ]
        widgets = {
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
            'medical_conditions': forms.Textarea(attrs={'rows': 3}),
            'allergies': forms.Textarea(attrs={'rows': 2}),
            'medications': forms.Textarea(attrs={'rows': 2}),
        }
    
    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
        
        # If editing existing student, populate user fields
        if self.instance.pk and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
            self.fields['date_of_birth'].initial = self.instance.user.date_of_birth
            self.fields['gender'].initial = self.instance.user.gender
            self.fields['phone_number'].initial = self.instance.user.phone_number
            self.fields['address'].initial = self.instance.user.address
            self.fields['city'].initial = self.instance.user.city
            self.fields['state'].initial = self.instance.user.state
            self.fields['postal_code'].initial = self.instance.user.postal_code
    
    def save(self, commit=True):
        student = super().save(commit=False)
        
        # Create or update user
        if student.user_id:
            user = student.user
        else:
            # Create new user
            username = self.cleaned_data['email'].split('@')[0]
            # Make username unique
            base_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            
            user = User.objects.create_user(
                username=username,
                email=self.cleaned_data['email'],
                password='student123',  # Default password
                role=User.UserRole.STUDENT
            )
        
        # Update user fields
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.gender = self.cleaned_data.get('gender')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.address = self.cleaned_data.get('address')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.postal_code = self.cleaned_data.get('postal_code')
        
        if commit:
            user.save()
            student.user = user
            student.save()
        
        return student
