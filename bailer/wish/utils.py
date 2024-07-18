from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client():
    subject="This email is from django server"
    message="This is a test message from django server mail"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["atishay1409@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)