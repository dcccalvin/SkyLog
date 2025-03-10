from django.urls import path
from . import views

app_name = 'logs'
urlpatterns = [
    path('logs_list/', views.log_list, name='logs_list'),
    path('logs/new/', views.create_log, name='create_log'),
    path('logs/<int:log_id>/edit/', views.edit_log, name='edit_log'), 
    path('logs/<int:log_id>/delete/', views.delete_log, name='delete_log'),  
]
