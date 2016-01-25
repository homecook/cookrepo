from .models import Meal, MealRating
from rest_framework import serializers

class MealBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('meal_id',
                  'meal_cook',
                  'meal_name',
                  'meal_available_date',
                  'meal_available_time',
                  'meal_expiry_date',
                  'meal_expiry_time')