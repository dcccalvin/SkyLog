from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.timezone import now
import uuid


icao_validator = RegexValidator(
    regex=r'^[A-Z]{4}$',
    message="Enter a valid 4-letter ICAO airport code (e.g., HKJK, EGLL).",
    code='invalid_icao'
)

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    date = models.DateField(default=now) 
    AIRCRAFT=[("General Aviation","General Aviation"),("Commercial","Commercial"),("Military","Military")] 
    aircraft = models.CharField(max_length=100,choices=AIRCRAFT)
    aircraft_type = models.CharField(max_length=100)
    aircraft_registration = models.CharField(max_length=100)
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

    
    flight_number = models.CharField(max_length=20, unique=True, default=uuid.uuid4)

    safety_concerns = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} | {self.aircraft} | {self.departure_airport} to {self.arrival_airport}"
