from datetime import datetime
from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    """ Form to place a booking """

    class Meta:
        """ Select model and set fields and labels """
        model = Booking
        fields = ('name', 'email', 'date', 'time',
                  'guests', 'special_request')
        labels = {
            'name': 'Name',
            'email': 'Email',
            'date': 'Date',
            'time': 'Time',
            'guests': 'Number of Guests',
            'special_request': 'Special Requests',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field'}),
            'email': forms.TextInput(attrs={'class': 'input-field'}),
            'date': forms.SelectDateWidget(attrs={'class': 'input-field'}),
            'time': forms.Select(attrs={'class': 'input-field'}),
            'guests': forms.NumberInput(attrs={'class': 'input-field'}),
            'special_request': forms.Textarea(attrs={'class': 'input-field'})
        }
