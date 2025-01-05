# forms.py
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = Registration
        fields = ['person_name', 'person_mobile_no', 'adhar_no', 'adhar_front', 'adhar_back', 
                  'institute_name', 'institute_govt_reg_no', 'institute_website', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        
        return cleaned_data
