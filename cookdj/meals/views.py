from django.shortcuts import render
from .serializers import MealBasicInfoSerializer, MealSerializer
from .models import Meal, MealRating
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

import ipdb


class MealViewSet(viewsets.ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @detail_route()
    def cooks_meals(self, request, cook_id):
        ''' Detailed route to get basic meal information of meals created by a particular cook
        :param request:
        :param cook_id: user_id of cook (corresponds to meal_cook in Meal model)
        :return:
        '''
        meals = self.queryset.filter(meal_cook=cook_id)
        serializer = MealBasicInfoSerializer(meals, many=True)      # override the default serializer
        return Response(serializer.data)