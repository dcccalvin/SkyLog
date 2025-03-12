# Generated by Django 4.2 on 2025-03-12 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logs', '0007_alter_log_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot_Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_class', models.CharField(choices=[('Class 1', 'Class 1'), ('Class 2', 'Class 2'), ('Class 3', 'Class 3')], max_length=20)),
                ('medical_certificate_number', models.CharField(max_length=20)),
                ('medical_certificate_issue_date', models.DateField()),
                ('medical_certificate_expiry_date', models.DateField()),
                ('license_type', models.CharField(choices=[('PPL', 'PPL'), ('CPL', 'CPL'), ('ATPL', 'ATPL')], max_length=20)),
                ('license_number', models.CharField(max_length=20)),
                ('license_issue_date', models.DateField()),
                ('license_expiry_date', models.DateField()),
                ('engine_rating', models.CharField(choices=[('Single Engine', 'Single Engine'), ('Multi Engine', 'Multi Engine')], max_length=20)),
                ('instrument_rating', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('night_rating', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
