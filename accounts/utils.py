from django.core.mail import EmailMessage
import random
from .models import User, OneTimePassword
from django.conf import settings

def send_generated_otp_to_email(email, request):
    otp = random.randint(100000, 999999)
    user = User.objects.get(email=email)
    otp_obj = OneTimePassword.objects.create(user=user, otp=otp)
    subject = "Your OTP for Verification"
    message = f"Your OTP is: {otp}"
    from_email = settings.DEFAULT_FROM_EMAIL
    receiver = email
    try:
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[receiver],
        )
        email.send()
        print("OTP Sent successfully to email.")
    except Exception as e:
        return e

def resend_otp_email(email, user, request):
    otp = random.randint(100000, 999999)
    current_otp = OneTimePassword.objects.get(user=user)
    current_otp.otp = otp
    current_otp.save()
    subject = "Resend OTP for Verification"
    message = f"Your new OTP is: {otp}"
    from_email = settings.DEFAULT_FROM_EMAIL
    receiver = email
    try:
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[receiver],
        )
        email.send()
        print("OTP Resent successfully to email.")
    except Exception as e:
        return e


def send_normal_email(data):

    message = data.get('email_body', '')
    subject = data.get('email_subject', '')
    receiver = data.get('to_email', '')
    from_email = data.get('from_email', '')
    # Now you can use these variables as needed

    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=from_email,
        to=[receiver],
    )
    email.send()


