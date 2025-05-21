from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, FileExtensionValidator
from django.utils.timezone import now
from django.core.exceptions import ValidationError
import re
import uuid



icao_validator = RegexValidator(
    regex=r'^[A-Z]{4}$',
    message="Enter a valid 4-letter ICAO airport code (e.g., HKJK, EGLL).",
    code='invalid_icao'
)
 
def is_aircraft_reg_num_valid(value):
    """
    Validates the aircraft registration number based on ICAO Annex 7 standards.
    """
    # General format validation: [1-2 alphanumeric prefix]-[1-5 alphanumeric suffix]
    pattern = r'^[A-Z0-9]{1,2}-[A-Z0-9]{1,5}$'
    
    if not re.match(pattern, value):
        raise ValidationError(
            "Invalid aircraft registration number. Ensure it follows the format: "
            "Country Prefix (1-2 letters/numbers) followed by a hyphen (-) and a Registration Suffix (1-5 alphanumeric characters)."
        )
    return value

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    date = models.DateTimeField(default=now)
    AIRCRAFT=[("General Aviation","General Aviation"),("Commercial","Commercial"),("Military","Military")] 
    aircraft = models.CharField(max_length=100,choices=AIRCRAFT)
    aircraft_type = models.CharField(max_length=100)
    aircraft_registration = models.CharField(max_length=100,validators=[is_aircraft_reg_num_valid])
    departure_airport = models.CharField(max_length=4, validators=[icao_validator])
    arrival_airport = models.CharField(max_length=4, validators=[icao_validator])
    flight_time = models.DurationField()  # timedelta for hours & minutes
    souls_on_board = models.PositiveIntegerField(default=0)
    fuel_on_departure = models.PositiveIntegerField(default=0)
    fuel_on_arrival = models.PositiveIntegerField(default=0)

    remarks = models.TextField(blank=True, null=True)
    PURPOSE=[("Training","Training"),
             ("Recreational","Recreational"),
             ("Cargo_flight","Cargo_flight"),
             ("Passenger_flight","Passenger_flight")
             ]
    purpose = models.CharField(max_length=20,choices=PURPOSE)

    
    FLIGHT_TYPES = [("VFR", "Visual Flight Rules"), ("IFR", "Instrument Flight Rules")]
    flight_type = models.CharField(max_length=3, choices=FLIGHT_TYPES)

    
    flight_number = models.CharField(max_length=80, unique=True, default=uuid.uuid4)

    safety_concerns = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} | {self.aircraft} | {self.departure_airport} to {self.arrival_airport} |--->{self.user}"
    
class PilotCertification(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    MEDICAL_CLASS=[("Class 1","Class 1"),("Class 2","Class 2"),("Class 3","Class 3")]
    medical_class=models.CharField(max_length=20,choices=MEDICAL_CLASS)
    medical_certificate_number=models.CharField(max_length=20)
    medical_certificate_issue_date=models.DateField()
    medical_certificate_expiry_date=models.DateField()
    LICENSE_TYPES=[("PPL","PPL"),("CPL","CPL"),("ATPL","ATPL")]
    license_type=models.CharField(max_length=20,choices=LICENSE_TYPES)
    license_number=models.CharField(max_length=20)
    license_issue_date=models.DateField()
    license_expiry_date=models.DateField()
    ENGINE_RATING=[("Single Engine","Single Engine"),("Multi Engine","Multi Engine")]
    engine_rating=models.CharField(max_length=20,choices=ENGINE_RATING)
    INSTRUMENT_RATING=[("Yes","Yes"),("No","No")]
    instrument_rating=models.CharField(max_length=20,choices=INSTRUMENT_RATING)
    NIGHT_RATING=[("Yes","Yes"),("No","No")]
    night_rating=models.CharField(max_length=20,choices=NIGHT_RATING)

    def __str__(self):
        return f"{self.user} | {self.license_type} | {self.engine_rating} | {self.instrument_rating} | {self.night_rating}"

class TrainingRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training_type = models.CharField(max_length=100)
    completion_date = models.DateField()
    instructor_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.training_type} ({self.completion_date})"


class FlightCrewAssignment(models.Model):
    log_entry = models.ForeignKey(Log, on_delete=models.CASCADE, related_name="crew_assignments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ROLE=[("Captain", "Captain"), ("First Officer", "First Officer"), ("Instructor", "Instructor"),("Flight Engineer","Flight Engineer")]
    role = models.CharField(max_length=50, choices=ROLE)
    number_of_crew = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.user} - {self.role} in Flight {self.log_entry.flight_number}"


class WeatherReport(models.Model):
    log_entry = models.ForeignKey(Log, on_delete=models.CASCADE)
    WEATHER_CONDITIONS=[("Clear","Clear"),("Cloudy","Cloudy"),("Rainy","Rainy"),("Foggy","Foggy"),("Snowy","Snowy"),("Windy","Windy"),("Rainy & Foggy","Rain & Foggy")]
    weather_conditions = models.CharField(max_length=100,choices=WEATHER_CONDITIONS)
    wind_speed = models.FloatField()  
    temperature = models.FloatField()  

    def __str__(self):
        return f"Weather for {self.log_entry.flight_number} - {self.weather_conditions}"


class EmergencyIncident(models.Model):
    log_entry = models.ForeignKey(Log, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=100)
    actions_taken = models.TextField()
    outcome = models.TextField()

    def __str__(self):
        return f"{self.incident_type} - {self.log_entry.flight_number}"


class MaintenanceReport(models.Model):
    log_entry = models.ForeignKey(Log, on_delete=models.CASCADE)  
    aircraft_registration = models.CharField(max_length=100)
    issue_reported = models.TextField()
    fix_details = models.TextField()

    def __str__(self):
        return f"Maintenance for {self.aircraft_registration} "


class FlightAttachment(models.Model):
    log_entry = models.ForeignKey(Log, on_delete=models.CASCADE)
    file = models.FileField(upload_to="attachments/",validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'docx'])])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Attachment for Flight {self.log_entry.flight_number}"
