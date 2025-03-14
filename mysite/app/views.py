from rest_framework.generics import CreateAPIView
from .models import ContactRequest
from .serializers import ContactRequestSerializer
from .tasks import send_contact_email


class ContactRequestCreateView(CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        phone_number_str = str(contact.phone_number)
        send_contact_email.delay(contact.name, phone_number_str)
