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
    path('certifications/', views.pilot_certification, name='pilot_certification'), 
    path('certifications/view/', views.view_pilot_certification, name='view_pilot_certification'),
]
