from django.urls import path
from .views import create_booking, success

urlpatterns = [
    path("", create_booking, name="create_booking"),
    path("success/", success, name="success"),
]