from django import forms
from django.core.exceptions import ValidationError
from .models import Organizer
from .validators import company_name


class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['company_name', 'phone_number', 'secret_key', 'website']
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter a company name...'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter a valid phone number (digits only)...'}),
            'secret_key': forms.PasswordInput(attrs={'placeholder': 'Enter a secret key like <1234>...'}),
            'website': forms.TextInput(attrs={'placeholder': 'Enter a company website...'}),
        }

    def clean_company_name(self):
        name = self.cleaned_data['company_name']
        try:
            company_name(name)
        except ValidationError as e:
            raise forms.ValidationError(e)
        if not (2 <= len(name) <= 110):
            raise forms.ValidationError('The company name must be between 2 and 110 characters.')
        return name

    def clean_secret_key(self):
        key = self.cleaned_data['secret_key']
        if not key.isdigit() or len(key) != 4 or len(set(key)) != 4:
            raise forms.ValidationError('Your secret key must have 4 unique digits!')
        return key