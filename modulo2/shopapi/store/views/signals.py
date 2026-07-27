# store/signals.py

import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from store.models.profile import UserProfile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    print(f"[SIGNAL] Usuario guardado: {instance.username}")

    if created:
        print(f"[SIGNAL] Nuevo usuario creado: {instance.email}")

        UserProfile.objects.create(user=instance)

        _send_welcome(instance)


def _send_welcome(user):
    """
    Envía correo de bienvenida.
    Falla en silencio para no bloquear el registro.
    """
    if not user.email:
        print("[EMAIL] El usuario no tiene correo.")
        return

    print(f"[EMAIL] Intentando enviar correo a: {user.email}")

    try:
        from store.services.email import send_welcome_email

        send_welcome_email(user)

        print(f"[EMAIL] Correo enviado correctamente a: {user.email}")

    except Exception as e:
        print(f"[EMAIL] ERROR enviando correo: {e}")
        logger.exception(
            "Error enviando correo de bienvenida a %s",
            user.email
        )