from django.urls import path
from .views import *

urlpatterns = [
    path('api/contact/', ContactRequestCreateView.as_view(), name='contact-api'),
]