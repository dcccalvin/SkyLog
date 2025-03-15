from django import forms
from .models import Log
from .models import PilotCertification, TrainingRecord, FlightCrewAssignment, WeatherReport, EmergencyIncident, MaintenanceReport, FlightAttachment
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import now
from django.utils.dateparse import parse_datetime
from django.core.exceptions import ValidationError

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['date', 'aircraft', 'aircraft_type', 'aircraft_registration', 
                  'departure_airport', 'arrival_airport', 'flight_time', 
                    'souls_on_board', 'fuel_on_departure', 'fuel_on_arrival',
                  'remarks', 'purpose', 'flight_type', 'safety_concerns']
    def clean_date(self):
        date_str = self.cleaned_data.get('date')  # Get the raw input

        if isinstance(date_str, str): 
            date = parse_datetime(date_str)  # Convert string to datetime
        else:
            date = date_str  # Use as-is if already a datetime object

        if not date:  # Ensure valid datetime
            raise ValidationError("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        

        if date > now():  # Ensure the date is not in the future
            raise ValidationError("The date cannot be in the future.")

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
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['medical_certificate_issue_date'] > cleaned_data['medical_certificate_expiry_date']:
            raise ValidationError("Medical certificate issue date cannot be after expiry date.")
        if cleaned_data['license_issue_date'] > cleaned_data['license_expiry_date']:
            raise ValidationError("License issue date cannot be after expiry date.")
            
        return cleaned_data


class TrainingRecordForm(forms.ModelForm):
    class Meta:
        model = TrainingRecord
        fields = ['training_type', 'completion_date', 'instructor_name']

class FlightCrewAssignmentForm(forms.ModelForm):
    class Meta:
        model = FlightCrewAssignment
        fields = ['role','number_of_crew']

class WeatherReportForm(forms.ModelForm):
    class Meta:
        model = WeatherReport
        fields = ['weather_conditions', 'temperature', 'wind_speed']

class EmergencyIncidentForm(forms.ModelForm):
    class Meta:
        model = EmergencyIncident
        fields = ['incident_type','actions_taken','outcome' ]



class FlightAttachmentForm(forms.ModelForm):
    class Meta:
        model = FlightAttachment
        fields = ['file', 'description']

class MaintenanceReportForm(forms.ModelForm):
    class Meta:
        model = MaintenanceReport
        fields = ['aircraft_registration','issue_reported','fix_details']


