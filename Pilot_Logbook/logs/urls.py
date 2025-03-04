from django.urls import path
from . import views

urlpatterns = [
    path('logs/', views.log_list, name='log_list'),
    path('logs/new/', views.create_log, name='create_log'),
]
