from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    " This serializes the django User class (django.contrib.auth.models.User), not the user details class."

    user_detail = serializers.StringRelatedField(read_only=True)
    meals_cook = serializers.StringRelatedField(many=True, read_only=True)
    meals_subscribe = serializers.StringRelatedField(many=True, read_only=True)
    orders = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
                  'id',
                  'username',
                  'email',
                  'user_detail',
                  'meals_cook',
                  'meals_subscribe',
                  'orders'
                  )

# TODO: Add a serializer to bring in information about orders and meals