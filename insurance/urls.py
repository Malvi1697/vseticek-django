from django.urls import path
from .views import insurance_home

urlpatterns = [
    path('', insurance_home, name='insurance_home')
    ]