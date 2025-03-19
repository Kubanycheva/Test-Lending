from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.core.mail import send_mail
from .models import ContactRequest, ClassImage, Img
from .serializers import ContactRequestSerializer, ClassImageSerializer, ImgSerializer


class ContactRequestCreateView(CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    def perform_create(self, serializer):
        contact_request = serializer.save()
        send_mail(
            'Новый запрос от клиента',
            f'Имя: {contact_request.name}\nТелефон: {contact_request.phone_number}',
            'lkybanucheva.com',  # Укажите адрес отправителя
            ['kubanycevalili@gmail.com'],  # Укажите email менеджера
            fail_silently=False,
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassImageViewSet(viewsets.ModelViewSet):
    queryset = ClassImage.objects.all()
    serializer_class = ClassImageSerializer


class ImgViewSet(viewsets.ModelViewSet):
    queryset = Img.objects.all()
    serializer_class = ImgSerializer

