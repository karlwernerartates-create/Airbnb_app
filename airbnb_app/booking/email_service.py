import resend
from django.conf import settings

resend.api_key = settings.RESEND_API_KEY


def send_admin_notification(booking):
    return resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": ["karlwernerartates@gmail.com"],  # <-- YOU
        "subject": "New Airbnb Booking",
        "html": f"""
            <h2>New Booking Received</h2>
            <p><b>Guest Email:</b> {booking.email}</p>
            <p><b>Property:</b> {booking.property.name}</p>
            <p><b>Date:</b> {booking.created_at}</p>
        """
    })