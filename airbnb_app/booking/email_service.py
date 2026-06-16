import resend
from django.conf import settings

resend.api_key = settings.RESEND_API_KEY


def send_admin_notification(booking):
    return resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": ["karlwernerartates@gmail.com"],
        "subject": "New Airbnb Booking",

        "html": f"""
            <h2>New Booking Received</h2>

            <p><strong>Guest Email:</strong> {booking.email}</p>
            <p><strong>Property:</strong> {booking.property.name}</p>
            <p><strong>Created At:</strong> {booking.created_at}</p>

            <hr>

            <p><strong>Contract Sent:</strong> {booking.contract_sent}</p>
            <p><strong>Contract Signed:</strong> {booking.contract_signed}</p>
        """
    })