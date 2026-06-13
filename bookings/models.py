from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    email = models.EmailField()

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    contract_sent = models.BooleanField(
        default=False
    )

    contract_signed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.email
