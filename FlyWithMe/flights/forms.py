from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_id', 'dep_airport', 'dep_date', 'dep_time', 'arr_airport', 'arr_date', 'arr_time']
