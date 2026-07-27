from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def _send(subject: str, to: str, txt_template: str, html_template: str, context: dict) -> None:
    text_body = render_to_string(txt_template, context)
    html_body = render_to_string(html_template, context)

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to],
    )

    msg.attach_alternative(html_body, 'text/html')

    print(f"[EMAIL] Enviando correo a: {to}")

    resultado = msg.send(fail_silently=False)

    print(f"[SMTP] Resultado: {resultado}")

    return resultado