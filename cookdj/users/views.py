from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import User, UserPaymentInfo

from .serializers import UserSerializer
from rest_framework import viewsets

# Basic django views

def test_home(request):
    return HttpResponse('this is homecook homepage!')

def test_user_details(request, user_id):
    '''
    Displays user details (if user exist, load and populate the details template)
    but otherwise render the invalid_user template
    :param request: request
    :param user_id: user_id
    :return: corresponding rendered template
    '''
    try:
        user = User.objects.get(user_id=user_id)
        full_name = user.user_fname + ' ' + user.user_lname
        return render_to_response("users/details.html", {'user_id': user_id, 'full_name': full_name})
    except Exception as err:
        print(err)
        return render_to_response("users/invalid_user.html", {'user_id': user_id})


# REST views

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer