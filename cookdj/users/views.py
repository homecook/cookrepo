from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import User, UserPaymentInfo

from .serializers import UserSerializer
from rest_framework import viewsets
import ipdb

# Basic django views

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer