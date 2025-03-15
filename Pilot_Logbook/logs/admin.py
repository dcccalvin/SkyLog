from django.contrib import admin
from .models import Log, PilotCertification, TrainingRecord, FlightCrewAssignment, WeatherReport, EmergencyIncident, MaintenanceReport, FlightAttachment
# Register your models here.

admin.site.register(Log)
admin.site.register(PilotCertification)
admin.site.register(TrainingRecord)
admin.site.register(FlightCrewAssignment)
admin.site.register(WeatherReport)
admin.site.register(EmergencyIncident)
admin.site.register(MaintenanceReport)
admin.site.register(FlightAttachment)
