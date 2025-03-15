from rest_framework.generics import CreateAPIView
from .models import ContactRequest
from .serializers import ContactRequestSerializer
from .tasks import send_contact_email

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from .models import ContactRequest
from .serializers import ContactRequestSerializer


@api_view(['POST'])
def contact_request(request):
    if request.method == 'POST':
        serializer = ContactRequestSerializer(data=request.data)

        if serializer.is_valid():
            # Сохраняем данные в базе
            contact_request = serializer.save()

            # Отправляем письмо менеджеру
            send_mail(
                'Новый запрос от клиента',
                f'Имя: {contact_request.name}\nТелефон: {contact_request.phone_number}',
                'lkybanucheva.com',  # Укажите адрес отправителя
                ['kubanycevalili@gmail.com'],  # Укажите email менеджера
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
