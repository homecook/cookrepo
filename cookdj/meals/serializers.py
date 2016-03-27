from .models import Meal
from rest_framework import serializers


class MealBasicInfoSerializer(serializers.ModelSerializer):
    # you can present orders in other ways (like StringRelatedField, PrimaryKeyRelatedField (default), etc.)
    # if more detailed/custom info necessary create a nested order serializer
    orders = serializers.StringRelatedField(many=True, read_only=True)
    meal_cook = serializers.ReadOnlyField(source='meal_cook.username')

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
                  'meal_num_servings_ordered',
                  'meal_is_available',
                  'meal_cooking_tommorow'
                  )


class MealSerializer(serializers.ModelSerializer):
    meal_cook = serializers.ReadOnlyField(source='meal_cook.username')  # Override the default foreign key to user

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
                    'meal_creation_datetime',
                    'meal_subscribers',
                    )