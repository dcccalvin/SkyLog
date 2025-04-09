from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Log
from .forms import LogForm
from django.db.models import Q
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .models import PilotCertification, TrainingRecord, FlightCrewAssignment, WeatherReport, EmergencyIncident, MaintenanceReport, FlightAttachment
from .forms import PilotCertificationForm, TrainingRecordForm, FlightCrewAssignmentForm, WeatherReportForm, EmergencyIncidentForm, MaintenanceReportForm, FlightAttachmentForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import capfirst
# Create your views here.


@login_required
def create_log(request):
    if request.method == "POST":
        log_form = LogForm(request.POST)  
        if log_form.is_valid():
            log = log_form.save(commit=False)
            log.user = request.user  
            log.save()
            return redirect('logs:add_additional_info', log_id=log.id) 
    else:
        log_form = LogForm()
    return render(request, 'logs/create_log.html', {'log_form': log_form})


@login_required
def log_list(request):
    logs = Log.objects.filter(user=request.user).order_by('-date')  
    query = request.GET.get('query')  
    if query:
        logs = logs.filter(
            Q(aircraft__icontains=query) |
            Q(aircraft_type__icontains=query) |
            Q(aircraft_registration__icontains=query) |
            Q(departure_airport__icontains=query) |
            Q(arrival_airport__icontains=query) |
            Q(flight_number__icontains=query) |
            Q(remarks__icontains=query)
        )
    return render(request, 'logs/log_list.html', {'logs': logs})

@login_required
def edit_log(request, log_id):
    log = get_object_or_404(Log, id=log_id, user=request.user)  
    
    if request.method == "POST":
        log_form = LogForm(request.POST, instance=log)
        if log_form.is_valid():
            log_form.save()  
            return redirect('logs:logs_list')
        else:
            print(log_form.errors)
    else:
        log_form = LogForm(instance=log)

    return render(request, 'logs/edit_log.html', {'log_form': log_form, 'log': log})


@login_required
def delete_log(request, log_id):
    log = get_object_or_404(Log, id=log_id, user=request.user)

    if request.method == "POST":
        log.delete()
        return redirect('logs:logs_list')

    return render(request, 'logs/delete_log.html', {'log': log})

@login_required
def generate_pdf_page(request):
    logs = Log.objects.filter(user=request.user).order_by('-date')
    return render(request, 'logs/generate_pdf.html', {'logs': logs})

@login_required
def generate_pdf(request):
    logs = Log.objects.filter(user=request.user).order_by('-date')
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Flight_logbook.pdf"'
    
    pdf = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y_position = height - 50

    pdf.setFont("Helvetica", 16)
    pdf.drawString(100, y_position, f"{capfirst(request.user.username)}'s Flight Logbook")
    pdf.setFont("Helvetica", 12)
    y_position -= 40

    for log in logs:
        # func to add new page if near the end of the page
        if y_position < 50:  
            pdf.showPage()
            y_position = height - 100
            pdf.setFont("Helvetica", 12)  

        pdf.drawString(50, y_position, f"Date: {log.date}")
        pdf.drawString(50, y_position - 20, f"Aircraft: {log.aircraft}")
        pdf.drawString(50, y_position - 40, f"Aircraft Type: {log.aircraft_type}")
        pdf.drawString(50, y_position - 60, f"Aircraft Registration: {log.aircraft_registration}")
        pdf.drawString(50, y_position - 80, f"Departure Airport: {log.departure_airport}")
        pdf.drawString(50, y_position - 100, f"Arrival Airport: {log.arrival_airport}")
        pdf.drawString(50, y_position - 120, f"Flight Time: {log.flight_time}")
        pdf.drawString(50, y_position - 140, f"Souls on Board: {log.souls_on_board}")
        pdf.drawString(50, y_position - 160, f"Fuel on Departure: {log.fuel_on_departure}")
        pdf.drawString(50, y_position - 180, f"Fuel on Arrival: {log.fuel_on_arrival}")
        pdf.drawString(50, y_position - 200, f"Remarks: {log.remarks}")
        pdf.drawString(50, y_position - 220, f"Purpose: {log.purpose}")
        pdf.drawString(50, y_position - 240, f"Flight Type: {log.flight_type}")
        pdf.drawString(50, y_position - 260, f"Flight Number: {log.flight_number}")
        pdf.drawString(50, y_position - 280, f"Safety Concerns: {log.safety_concerns}")

        # Move position down for next log entry
        y_position -= 400  

    pdf.save()
    return response

@login_required
def pilot_certification(request):
    certification, created = PilotCertification.objects.get_or_create(
        user=request.user,
        defaults={
            "medical_certificate_issue_date": timezone.now().date(),
            "medical_certificate_number": "000000",
            "medical_class": "Class 1",  
            "medical_certificate_expiry_date": timezone.now().date(),
            "license_type": "PPL",  
            "license_number": "000000",
            "license_issue_date": timezone.now().date(),
            "license_expiry_date": timezone.now().date(),
            "engine_rating": "Single Engine",  
            "instrument_rating": "No",  
            "night_rating": "No",  
        }
    )

    if request.method == "POST":
        pilot_certification_form = PilotCertificationForm(request.POST, instance=certification)
        if pilot_certification_form.is_valid():
            pilot_certification_form.save()
            return redirect('logs:view_pilot_certification')

    else:
        pilot_certification_form = PilotCertificationForm(instance=certification)

    return render(request, 'certification/pilot_certification.html', {'pilot_certification_form': pilot_certification_form})

@login_required
def view_pilot_certification(request):
    certification = get_object_or_404(PilotCertification, user=request.user)
    return render(request, 'certification/view_pilot_certification.html', {'certification': certification}) 

# --- Training Records ---
@login_required
def create_training_record(request):
    if request.method == "POST":
        form = TrainingRecordForm(request.POST)
        if form.is_valid():
            training_record = form.save(commit=False)
            training_record.user = request.user
            training_record.save()
            return redirect('logs:training_record_list')
    else:
        form = TrainingRecordForm()
    return render(request, 'logs/training/create.html', {'form': form})

@login_required
def list_training_records(request):
    records = TrainingRecord.objects.filter(user=request.user)
    return render(request, 'logs/training/list.html', {'records': records})

@login_required
def add_additional_info(request, log_id):
    log_entry = get_object_or_404(Log, id=log_id, user=request.user)

    if request.method == "POST":
        crew_form = FlightCrewAssignmentForm(request.POST)
        weather_form = WeatherReportForm(request.POST)
        incident_form = EmergencyIncidentForm(request.POST)
        attachment_form = FlightAttachmentForm(request.POST, request.FILES)
        maintenance_form = MaintenanceReportForm(request.POST)

        if all([crew_form.is_valid(), weather_form.is_valid(), incident_form.is_valid(), attachment_form.is_valid(), maintenance_form.is_valid()]):
            crew = crew_form.save(commit=False)
            crew.log_entry = log_entry
            crew.user = request.user
            crew.save()

            weather = weather_form.save(commit=False)
            weather.log_entry = log_entry
            weather.save()

            incident = incident_form.save(commit=False)
            incident.log_entry = log_entry
            incident.save()

            attachment = attachment_form.save(commit=False)
            attachment.log_entry = log_entry
            attachment.save()

            maintenance = maintenance_form.save(commit=False)
            maintenance.log_entry = log_entry
            maintenance.save()

            return redirect('logs:logs_list')  # Redirect after completion

    else:
        crew_form = FlightCrewAssignmentForm()
        weather_form = WeatherReportForm()
        incident_form = EmergencyIncidentForm()
        attachment_form = FlightAttachmentForm()
        maintenance_form = MaintenanceReportForm()

    return render(request, 'logs/add_additional_info.html', {
        'crew_form': crew_form,
        'weather_form': weather_form,
        'incident_form': incident_form,
        'attachment_form': attachment_form,
        'maintenance_form': maintenance_form,
        'log_entry': log_entry,
    })


@login_required
def summary_report_pdf(request):
    logs = Log.objects.filter(user=request.user)
    total_flights = logs.count()
    total_hours = sum(log.flight_time for log in logs if log.flight_time)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Summary_Report.pdf"'

    pdf = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    pdf.setFont("Helvetica", 16)
    pdf.drawString(100, height - 50, f"{capfirst(request.user.username)}'s Flight Summary Report")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 100, f"Total Flights: {total_flights}")
    pdf.drawString(50, height - 120, f"Total Hours Flown: {total_hours:.2f}")

    pdf.save()
    return response