from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
import ipdb

# Basic django views

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer