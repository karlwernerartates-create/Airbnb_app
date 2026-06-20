from django.contrib import admin
from .models import Property, Booking

admin.site.register(Property)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "property",
        "contract_sent",
        "contract_signed",
        "created_at",
    )