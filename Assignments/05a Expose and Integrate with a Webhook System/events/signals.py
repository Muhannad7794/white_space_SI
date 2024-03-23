from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Event 


@receiver(post_save, sender=Event)
def notify_subscribers(sender, instance, created, **kwargs):
    topic = instance.topic
    subscribers = topic.subscribed_users.all()

    for sub in subscribers:
        send_mail(
            subject=f"Update on a topic you're subscribed to: {topic.name}",
            message=f"An event you're subscribed to has been {'created' if created else 'updated'}: {instance.name} on {instance.date}.",
            from_email="from@example.com",
            recipient_list=[sub.user.email],
        )
