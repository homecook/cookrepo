from django.shortcuts import render

# Create your views here.

def user_initialize(request, userid):
    # include user initlizations
    # but probably should be done as a class based view
    # with def __init__(self)
    return render(request, 'user_init.html', {'user_id': userid})