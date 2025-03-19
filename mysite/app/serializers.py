from rest_framework import serializers
from .models import *


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ['name', 'phone_number']


class ClassImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassImage
        fields = ['class_img']


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = ['img']
