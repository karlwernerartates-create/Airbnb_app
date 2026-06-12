import resend
from django.conf import settings

resend.api_key = settings.RESEND_API_KEY


def send_booking_notification(booking):
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": ["karlwernerartates@gmail.com"],
        "subject": "New Airbnb Booking",
        "html": f"""
        <h2>New Booking Received</h2>

        <p><strong>Guest Email:</strong> {booking.email}</p>
        <p><strong>Property:</strong> {booking.property.name}</p>
        <p><strong>Submitted:</strong> {booking.created_at}</p>
        """
    })