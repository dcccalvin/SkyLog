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
 
def is_aircraft_reg_num_valid(reg_num: str)  -> bool:
    split_reg_num = reg_num.split('-')

    # check if it is splited correctly using '-'
    if len(split_reg_num) != 2:
        return False
    
    # Check if the first part is alphanumeric and has 1 to 2 characters (country code)
    if not split_reg_num[0].isalnum() or len(split_reg_num[0]) not in [1, 2]:
        return False
    
    # Check if the second part is alphanumeric and has 3 to 5 characters
    if not split_reg_num[1].isalnum() or len(split_reg_num[1]) not in [3, 5]:
        return False
    
    return True

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    date = models.DateTimeField(default=now)
    AIRCRAFT=[("General Aviation","General Aviation"),("Commercial","Commercial"),("Military","Military")] 
    aircraft = models.CharField(max_length=100,choices=AIRCRAFT)
    aircraft_type = models.CharField(max_length=100)
    #will add validator later
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
