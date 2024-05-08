# myapp/views.py

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        # User is logged in, display their email
        return HttpResponse(f"Welcome to the app, you have successfully logged in using {request.user.email}")
    else:
        # User is not logged in, prompt to login or sign up
        return HttpResponse("Welcome to the Home Page! Please use /accounts/login/ to log in or sign up.")

