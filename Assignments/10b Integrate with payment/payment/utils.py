# payment/utils.py
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def simulate_stripe_payment():
    try:
        # Simulate a payment intent creation
        payment_intent = stripe.PaymentIntent.create(
            amount=1000,  # $10, for example
            currency="usd",
            payment_method_types=["card"],
            receipt_email="test@example.com",
        )
        print("Stripe payment intent created:", payment_intent.id)
    except stripe.error.StripeError as e:
        print("Stripe error:", str(e))
