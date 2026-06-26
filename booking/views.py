from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Booking
from .email_service import send_admin_notification


def create_booking(request):
    properties = Property.objects.all()

    return render(
        request,
        "booking/create_booking.html",
        {
            "properties": properties,
            "debug": list(properties.values()),
        },
    )


def success(request):
    return render(request, "booking/success.html")