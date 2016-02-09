from django.shortcuts import render
from .serializers import MealBasicInfoSerializer, MealSerializer
from .models import Meal, MealRating
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
import ipdb


@api_view(['GET'])
def cook_meals_view(request, cook_id, format=None):
    '''
    Displays basic meal information for a particular cook (user_id)
    :param request: request
    :param cook_id: cook's user_id
    :return: corresponding rendered template
    '''

    if request.method == 'GET':
        meals = Meal.objects.filter(meal_cook=cook_id)      # get list of meals created by cook
        serializer = MealBasicInfoSerializer(meals, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def meal_detail(request, meal_id=None, format=None):
    """
    Retrieve, create, update or delete a meal instance
    :param meal_id: primary id of meal if it's supplied (for GET, PUT, DELTE request types)
    :param format: which response data format to use
    """

    if request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        meal = Meal.objects.get(pk=meal_id)
    except Meal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MealSerializer(meal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
