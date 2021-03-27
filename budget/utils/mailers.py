from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


class VerificationMail:
    """
    Class for sending user verification email
    """

    def __init__(self, user, token):
        self.user = user
        self.token = token
        self.message = None

    def compose_mail(self):
        """
        Compose the email
        """
        html_body = render_to_string(
            template_name="verification.html",
            context={
                "name": self.user.username,
                "url": settings.VERIFICATION_URL + self.token,
            },
        )
        self.message = EmailMultiAlternatives(
            subject="Welcome {}".format(self.user.username),
            body="Verification mail",
            from_email=settings.DEFAULT_EMAIL,
            to=[self.user.email],
        )
        self.message.attach_alternative(html_body, "text/html")

    def send_mail(self):
        """
        Send the email
        """
        self.compose_mail()
        self.message.send()
