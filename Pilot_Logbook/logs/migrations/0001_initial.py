# Generated by Django 4.2 on 2025-03-04 10:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('aircraft', models.CharField(max_length=100)),
                ('aircraft_type', models.CharField(max_length=100)),
                ('aircraft_registration', models.CharField(max_length=100)),
                ('departure_airport', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_icao', message='Enter a valid 4-letter ICAO airport code (e.g., HKJK, EGLL).', regex='^[A-Z]{4}$')])),
                ('arrival_airport', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_icao', message='Enter a valid 4-letter ICAO airport code (e.g., HKJK, EGLL).', regex='^[A-Z]{4}$')])),
                ('flight_time', models.DurationField()),
                ('remarks', models.TextField(blank=True, null=True)),
                ('purpose', models.CharField(choices=[('Training', 'Training'), ('Recreational', 'Recreational'), ('Cargo_flight', 'Cargo_flight'), ('Passenger_flight', 'Passenger_flight')], max_length=20)),
                ('flight_type', models.CharField(choices=[('VFR', 'Visual Flight Rules'), ('IFR', 'Instrument Flight Rules')], max_length=3)),
                ('flight_number', models.CharField(default=uuid.uuid4, max_length=20, unique=True)),
                ('safety_concerns', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
