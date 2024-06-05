# payment/views.py

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["POST"])
def initiate_payment(request):
    # Simulating payment processing
    print("Payment initiated")  # Terminal output for simulation
    # Trigger webhook to confirm payment
    webhook_url = "http://127.0.0.1:8000/api/webhook/"  # Normally, this would be an external service's URL
    data = {"status": "success", "transaction_id": "12345"}
    # In real scenarios, use requests.post(webhook_url, json=data) here
    print(
        f"Webhook would be sent to: {webhook_url} with data: {data}"
    )  # Simulated webhook call
    return JsonResponse(
        {"status": "Payment simulated successfully"}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
def webhook_listener(request):
    # Endpoint for handling webhook calls
    print("Received webhook data:", request.data)  # Print received data to terminal
    return JsonResponse({"status": "Webhook received"}, status=status.HTTP_200_OK)
