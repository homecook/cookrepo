from django.shortcuts import render
from .serializers import MealBasicInfoSerializer
from .models import Meal, MealRating
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import ipdb

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def cook_meals_view(request, cook_id):
    '''
    Displays basic meal information for a particular cook (user_id)
    :param request: request
    :param user_id: user_id
    :return: corresponding rendered template
    '''

    try:
        meals = Meal.objects.get(meal_cook=cook_id)
        print(meals)
    except Meal.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MealBasicInfoSerializer(meals, context={'request': request})
        return JSONResponse(serializer.data)


class MealViewSet(viewsets.ModelViewSet):
    """
    Get all meals
    """
    queryset = Meal.objects.all()
    serializer_class = MealBasicInfoSerializer
