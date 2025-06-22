from django import forms
from event.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'slogan': forms.TextInput(attrs={'placeholder': 'Provide an appealing text...'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location...'}),
            'available_tickets': forms.NumberInput(attrs={'min': '0'}),
            'key_features': forms.Textarea(attrs={'placeholder': 'Provide important event details...'}),
            'banner_url': forms.URLInput(attrs={'placeholder': 'An optional banner image URL...'}),
        }

    def clean_slogan(self):
        slogan = self.cleaned_data['slogan']
        if not (2 <= len(slogan) <= 120):
            raise forms.ValidationError('Slogan must be between 2 and 120 characters.')
        return slogan

    def clean_location(self):
        location = self.cleaned_data['location']
        if not (2 <= len(location) <= 120):
            raise forms.ValidationError('Location must be between 2 and 120 characters.')
        return location