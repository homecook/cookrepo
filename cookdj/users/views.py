from django.shortcuts import render
from rest_framework import generics
from users.serializers import UserSerializer
from users.models import User

# Create your views here.

def user_test(request, userid):
    # include user initlizations
    # but probably should be done as a class based view
    # with def __init__(self)
    return render(request, 'user_init.html', {'user_id': userid})


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer