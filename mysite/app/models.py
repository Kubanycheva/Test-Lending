from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactRequest(models.Model):
    name = models.CharField(max_length=32)
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.name


class Img(models.Model):
    img = models.ImageField(upload_to='class_img/', null=True, blank=True)


class ClassImage(models.Model):
    class_img = models.ForeignKey(Img, on_delete=models.CASCADE, null=True, blank=True, related_name='class_images')
    image = models.ImageField(upload_to='image')
