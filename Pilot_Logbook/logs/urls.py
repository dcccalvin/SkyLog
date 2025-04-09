from django.urls import path
from . import views

app_name = 'logs'
urlpatterns = [
    path('logs_list/', views.log_list, name='logs_list'),
    path('logs/new/', views.create_log, name='create_log'),
    path('logs/<int:log_id>/edit/', views.edit_log, name='edit_log'), 
    path('logs/<int:log_id>/delete/', views.delete_log, name='delete_log'),
    path('logs/generate-pdf-page/', views.generate_pdf_page, name='generate_pdf_page'), 
    path('logs/generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('logs/summary_report_pdf/', views.summary_report_pdf, name='summary_report_pdf'),
    path('certifications/', views.pilot_certification, name='pilot_certification'), 
    path('certifications/view/', views.view_pilot_certification, name='view_pilot_certification'),
    path('training/create/', views.create_training_record, name='create_training_record'),
    path('training/', views.list_training_records, name='training_record_list'),
    path('log/<int:log_id>/additional-info/', views.add_additional_info, name='add_additional_info'),
]
