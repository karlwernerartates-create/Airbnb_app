from django.urls import path
from .views import booking_form, success

urlpatterns = [
    path('', booking_form, name='booking_form'),
    path('success/', success, name='success'),
]