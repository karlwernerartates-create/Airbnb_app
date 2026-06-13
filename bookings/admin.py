from django.contrib import admin
from .models import Property, Booking


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "property",
        "contract_sent",
        "contract_signed",
        "created_at",
    )

    list_filter = (
        "contract_sent",
        "contract_signed",
    )
