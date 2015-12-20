from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Meal(models.Model):
    '''
    Houses universe of (mostly static) information about meals.
    Information available as of meal creation
    '''

    SPICE_CHOICES = [('L', 'Mild'), ('M', 'Medium'), ('H', 'Hot')]

    CUSINE_CHOICES = [('Indian', 'Indian'),
                      ('Spanish', 'Spanish'),
                      ('Italian', 'Italian'),
                      ('European', 'European'),
                      ('American', 'American'),
                      ('Asian', 'Asian'),
                      ('Other', 'Other')]

    MEALTYPE_CHOICES = [('Breakfast', 'Breakfast'),
                        ('Brunch', 'Brunch'),
                        ('Lunch', 'Lunch'),
                        ('Dinner', 'Dinner'),
                        ('Dessert', 'Dessert'),
                        ('Other', 'Other')]

    meal_id = models.AutoField(primary_key=True)
    meal_cook = models.ForeignKey('users.User')  # can further validate that user is indeed a cook..
    meal_name = models.CharField(max_length=150)   # short meal name
    meal_description = models.TextField(blank=True, default='')
    meal_available_date = models.DateField(blank=False)
    meal_available_time = models.TimeField(blank=False)
    meal_expiry_date = models.DateField(blank=False)
    meal_expiry_time = models.TimeField(blank=False)
    meal_price = models.DecimalField(blank=False, max_digits=2, decimal_places=0)
    meal_servings = models.IntegerField(blank=False)
    meal_gluent_free = models.BooleanField(default=False)
    meal_nut_free = models.BooleanField(default=False)
    meal_lactose_free = models.BooleanField(default=False)
    meal_spice_level = models.CharField(choices=SPICE_CHOICES, max_length=240)
    meal_cusine = models.CharField(choices=CUSINE_CHOICES, default='Other', max_length=240)
    meal_mealtype = models.CharField(choices=MEALTYPE_CHOICES, default='Other', max_length=240)
    meal_creation_datetime = models.DateTimeField(blank=False, default=timezone.now())
    meal_modification_datetime = models.DateTimeField(blank=False, default=timezone.now())

    def __str__(self):
        return self.meal_name

    def cooking_tommorow(self):
        flag =  not self.meal_expired() and self.meal_available_date == timezone.now().date() + datetime.timedelta(days=1)
        return flag

    def cooking_next_10_days(self):
        flag = not self.meal_expired() and self.meal_available_date <= timezone.now().date() + datetime.timedelta(days=10)
        return flag

    def meal_expired(self):
        return timezone.now() >= self.meal_expiry_date

    # TODO: implement validators for basic information

class MealRating(models.Model):
    '''
    Store ratings, and *MUST* link to orders -> meals -> cooks (Analyze cook performance), and also orders -> eaters (analyze eater preference)
    '''

    RATING_CHOICES = [(1, 'Terrible'),
                      (2, 'Meh'),
                      (3, 'Good'),
                      (4, 'Nice!'),
                      (5, 'Como Casa!!!'),
                      (0, 'Unrated/NA')
                      ]

    rating_order = models.OneToOneField('orders.Order')    # Each order can only be rated once../or reviewed..becomes primary key..
    rating_meal = models.ForeignKey(Meal)    # Must be able to link to a meal
    rating_user = models.ForeignKey('users.User')    # Must be able to link to a user (TODO: Can't be cook!)

    # Rating on 4 basic dimensions: taste, value, service, punctuality
    rating_value = models.IntegerField(choices=RATING_CHOICES)  # could make this comma seperated integers, but have to do more validation
    rating_service = models.IntegerField(choices=RATING_CHOICES)
    rating_time = models.IntegerField(choices=RATING_CHOICES)
    rating_taste = models.IntegerField(choices=RATING_CHOICES)
