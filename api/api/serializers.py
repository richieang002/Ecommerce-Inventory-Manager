from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    firstname = serializers.CharField(write_only=True)
    lastname = serializers.CharField(write_only=True)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.validated_data.get('firstname', '')
        user.last_name = self.validated_data.get('lastname', '')
        user.save()
        return user
