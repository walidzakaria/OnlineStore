from django.core.mail import send_mail


def email(subject, message, sender, receiver):
    send_mail(
        subject, message, sender, receiver, fail_silently=False
    )