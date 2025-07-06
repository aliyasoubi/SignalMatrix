# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.btc_signals, name='btc_signals_dashboard'),
]
