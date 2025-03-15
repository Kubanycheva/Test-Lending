from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactRequest(models.Model):
    name = models.CharField(max_length=32)
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.name
