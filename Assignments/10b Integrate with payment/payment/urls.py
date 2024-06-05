# payment/urls.py

from django.urls import path
from .views import initiate_payment, webhook_listener

urlpatterns = [
    path("pay/", initiate_payment, name="initiate-payment"),
    path("webhook/", webhook_listener, name="webhook-listener"),  # Webhook endpoint
]
