from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth.models import User

from django.core.mail import EmailMultiAlternatives

def send_mail_to_client():
    subject = "this is from Django server"
    message = f""
    from_email = settings.EMAIL_HOST_USER
    users = User.objects.all()
    recipient_list = [x for x in users]

    send_mail(subject,message,from_email,recipient_list)
