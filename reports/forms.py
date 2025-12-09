from django import forms
from academics.models import Class, Section

class StudentReportFilterForm(forms.Form):
    class_group = forms.ModelChoiceField(
        queryset=Class.objects.all().order_by('numeric_value'),
        required=False,
        label='Class',
        empty_label="All Classes",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    section = forms.ModelChoiceField(
        queryset=Section.objects.all(),
        required=False,
        label='Section',
        empty_label="All Sections",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    gender = forms.ChoiceField(
        choices=[('', 'All Genders'), ('M', 'Male'), ('F', 'Female')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    status = forms.ChoiceField(
        choices=[('', 'All Status'), ('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('GRADUATED', 'Graduated')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Dynamic filtering of sections if class is selected (requires JS mainly, but initial filtering possible)
