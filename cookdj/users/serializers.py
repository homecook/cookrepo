from .models import User, UserPaymentInfo
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User