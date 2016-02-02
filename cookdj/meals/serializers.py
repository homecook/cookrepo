from .models import Meal, MealRating
from rest_framework import serializers


class MealBasicInfoSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)      # reverse relationship to Order object

    class Meta:
        model = Meal
        fields = ('meal_id',
                  'meal_cook',
                  'meal_name',
                  'meal_available_date',
                  'meal_available_time',
                  'meal_expiry_date',
                  'meal_expiry_time',
                  'meal_servings',
                  'orders',
                  'meal_num_orders',
                  'meal_num_servings_ordered')


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = (  'meal_id',
                    'meal_cook',
                    'meal_name',
                    'meal_description',
                    'meal_available_date',
                    'meal_available_time',
                    'meal_expiry_date',
                    'meal_expiry_time',
                    'meal_price',
                    'meal_servings',
                    'meal_gluent_free',
                    'meal_nut_free',
                    'meal_lactose_free',
                    'meal_spice_level',
                    'meal_cusine',
                    'meal_mealtype',
                    'meal_creation_datetime')