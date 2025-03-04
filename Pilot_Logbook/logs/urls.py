from django.urls import path
from . import views

app_name = 'logs'
urlpatterns = [
    path('logs_list/', views.log_list, name='logs_list'),
    path('logs/new/', views.create_log, name='create_log'),
]
