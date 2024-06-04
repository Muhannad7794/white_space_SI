# payment/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["POST"])
def initiate_payment(request):
    # Simulating payment processing
    return Response(
        {"status": "Payment simulated successfully"}, status=status.HTTP_200_OK
    )
