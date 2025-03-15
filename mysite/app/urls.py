from django.urls import path
from .views import ContactRequestCreateView

urlpatterns = [
    path('api/contact/', ContactRequestCreateView.as_view(), name='contact-api'),
]