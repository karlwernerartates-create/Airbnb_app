from django.shortcuts import render, redirect
from .forms import BookingForm
from .email_service import send_booking_notification


def booking_form(request):

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save()

            send_booking_notification(booking)

            return redirect("success")

    else:
        form = BookingForm()

    return render(
        request,
        "bookings/form.html",
        {"form": form}
    )


def success(request):
    return render(request, "bookings/success.html")