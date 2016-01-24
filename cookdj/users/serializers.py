from .models import User, UserPaymentInfo
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_fname', 'user_lname', 'user_email', 'user_address')