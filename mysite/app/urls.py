from django.urls import path
from .views import *

urlpatterns = [
    path('api/contact/', contact_request, name='contact-api'),
]