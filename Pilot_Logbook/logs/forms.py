from django import forms
from .models import Log
from .models import PilotCertification

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['date', 'aircraft', 'aircraft_type', 'aircraft_registration', 
                  'departure_airport', 'arrival_airport', 'flight_time', 
                    'souls_on_board', 'fuel_on_departure', 'fuel_on_arrival',
                  'remarks', 'purpose', 'flight_type', 'safety_concerns']
        
class PilotCertificationForm(forms.ModelForm):
    class Meta:
        model = PilotCertification
        fields = ['medical_class', 'medical_certificate_number','medical_certificate_issue_date',
                  'medical_certificate_expiry_date','license_type','license_number',
                  'license_issue_date','license_expiry_date','engine_rating','instrument_rating',
                  'night_rating'
                  ]

