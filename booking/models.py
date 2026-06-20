from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name


class Booking(models.Model):
    email = models.EmailField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    # Contract tracking (future DocuSeal integration)
    contract_sent = models.BooleanField(default=False)
    contract_signed = models.BooleanField(default=False)

    def __str__(self):
        return self.email