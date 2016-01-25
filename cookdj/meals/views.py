from django.shortcuts import render
from .serializers import MealBasicInfoSerializer
from .models import Meal, MealRating
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

import ipdb

@api_view(['GET', 'POST'])
def cook_meals_view(request, cook_id):
    '''
    Displays basic meal information for a particular cook (user_id)
    :param request: request
    :param cook_id: cook's user_id
    :return: corresponding rendered template
    '''

    if request.method == 'GET':
        meals = Meal.objects.filter(meal_cook=cook_id)
        serializer = MealBasicInfoSerializer(meals, context={'request': request}, many=True)
        return Response(serializer.data)


class MealViewSet(viewsets.ModelViewSet):
    """
    Get all meals
    """
    queryset = Meal.objects.all()
    serializer_class = MealBasicInfoSerializer
