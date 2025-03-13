from django import forms
from .models import Log
from .models import PilotCertification
from django.utils.timezone import now

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['date', 'aircraft', 'aircraft_type', 'aircraft_registration', 
                  'departure_airport', 'arrival_airport', 'flight_time', 
                    'souls_on_board', 'fuel_on_departure', 'fuel_on_arrival',
                  'remarks', 'purpose', 'flight_type', 'safety_concerns']
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date > now():
            raise forms.ValidationError("The date cannot be in the future.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        fuel_on_departure = cleaned_data.get("fuel_on_departure")
        fuel_on_arrival = cleaned_data.get("fuel_on_arrival")

        if fuel_on_departure is not None and fuel_on_arrival is not None:
            if fuel_on_arrival > fuel_on_departure:
                raise forms.ValidationError("Fuel on arrival cannot be more than fuel on departure.")
        return cleaned_data
        
class PilotCertificationForm(forms.ModelForm):
    class Meta:
        model = PilotCertification
        fields = ['medical_class', 'medical_certificate_number','medical_certificate_issue_date',
                  'medical_certificate_expiry_date','license_type','license_number',
                  'license_issue_date','license_expiry_date','engine_rating','instrument_rating',
                  'night_rating'
                  ]

