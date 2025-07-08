from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def send_booking_confirmation(self, recipient_email, booking_details):
    subject = 'Booking Confirmation'
    message = f'Thank you for your booking!\n\nDetails:\n{booking_details}'
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient_email],
        fail_silently=False,
    )
    return f"Email sent to {recipient_email}"