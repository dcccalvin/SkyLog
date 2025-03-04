from django import forms
from .models import Log

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['date', 'aircraft', 'aircraft_type', 'aircraft_registration', 
                  'departure_airport', 'arrival_airport', 'flight_time', 
                    'soul_on_board', 'fuel_on_departure', 'fuel_on_arrival',
                  'remarks', 'purpose', 'flight_type', 'safety_concerns']
