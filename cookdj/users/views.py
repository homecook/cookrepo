from django.contrib.auth.models import User
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import ipdb

# Basic django views

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def user_login(request, email, password):
    """
    User login
    """
    try:
        user = User.objects.get(email=email)
        if password == 'asdfghjkl':     # replace with an actual check for password when that's possible..
            serializer = UserLoginSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)    # return error if password does not match
            # TODO: replace with an actual authentication
            # serializer = UserLoginSerializer(user)
            # return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   # return error if user not found
