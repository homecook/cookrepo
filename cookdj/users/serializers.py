from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('user_id', 'user_email', 'user_fname', 'user_lname')

