from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Booking
from .email_service import send_admin_notification


def create_booking(request):
    properties = Property.objects.all()

    print("Properties:", list(properties.values()))
    print("Count:", properties.count())

    if request.method == "POST":
        email = request.POST.get("email")
        property_id = request.POST.get("property_id")

        property_obj = get_object_or_404(Property, id=property_id)

        booking = Booking.objects.create(
            email=email,
            property=property_obj
        )

        send_admin_notification(booking)

        return redirect("success")

    return render(
        request,
        "booking/create_booking.html",
        {"properties": properties}
    )


def success(request):
    return render(request, "booking/success.html")