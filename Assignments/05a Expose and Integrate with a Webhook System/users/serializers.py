from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        self.send_verification_email(user)
        return user

    def send_verification_email(self, user):
        token = default_token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        verify_url = reverse("verify_email", args=[uidb64, token])
        full_verify_url = f"{settings.SITE_DOMAIN}{verify_url}"
        send_mail(
            "Verify your account",
            f"Please use the following link to verify your account: {full_verify_url}",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
