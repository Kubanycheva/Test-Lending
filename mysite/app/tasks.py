from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_contact_email(name, phone_number):
    subject = "Новый контактный запрос"
    message = f"Имя: {name}\nТелефон: {phone_number}"
    recipient_email = settings.EMAIL_RECIEVER

    if recipient_email:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False,
        )