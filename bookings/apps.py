from django.apps import AppConfig


class BookingsConfig(AppConfig):
    name = 'bookings'

import os

RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")