from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
import datetime

class Users(models.Model):
    '''
    Houses basic (mostly static) user information
    '''

    PROVINCE_CHOICES = [('AB', 'Alberta'),
                       ('BC', 'British Columbia'),
                       ('MN', 'Manitoba'),
                       ('NB', 'New Brunswick'),
                       ('NS', 'Nova Scotia'),
                       ('ON', 'Ontario'),
                       ('PE', 'Prince Edward Island'),
                       ('QC', 'Quebec'),
                       ('SK', 'Saskatchewan'),
                       ('YK', 'Yukon'),
                       ('NU', 'Nunavut'),
                       ('NT', 'Northwest Territories')
                      ]

    user_id = models.AutoField(primary_key=True)
    user_email = models.EmailField(blank=False)
    user_pass = models.CharField(blank=False, max_length=8)  # do validation
    user_fname = models.CharField(blank=False, max_length=240)
    user_lname = models.CharField(blank=False, max_length=240)
    user_address = models.CharField(blank=False, max_length=240)
    user_city = models.CharField(blank=False, max_length=240)
    user_prov = models.CharField(choices = PROVINCE_CHOICES, max_length=240)
    user_country = models.CharField(blank=False, max_length=240)
    user_phone_mobile = models.CharField(blank=True, max_length=240, default='')
    user_phone_home = models.CharField(blank=True, max_length=240, default='')
    user_payment_verified = models.BooleanField(default=False)

    def __str__(self):
        full_name = self.user_fname + ' ' + self.user_lname
        return full_name

    # TODO: implement validators for basic information


class UserPaymentInfo(models.Model):
    '''
    Contains the user financial account information for payments(eating) and receive(cooking).
    Structure such that each row is an account
    '''

    ACCOUNT_CHOICES = [('Visa', 'Visa'),
                      ('Master', 'Mastercard'),
                      ('Amex', 'AMEX'),
                      ('Bank', 'Bank Account'),
                      ]

    payment_user = models.ForeignKey(Users)
    payment_default_pay = models.BooleanField(default=False)
    payment_default_receive = models.BooleanField(default=False)
    payment_account_type = models.CharField(choices=ACCOUNT_CHOICES, max_length=240)
    payment_account_info = models.CommaSeparatedIntegerField(max_length=240)   # ACCOUNT_NUMBER, SECURITY_CODE OR #ACCOUNT_NUMBER OR ACCOUNT_NUMBER, BRANCH_NUMBER
    payment_account_expiry = models.CommaSeparatedIntegerField(max_length=7) # YYYY,MM (e.g. 2018,05)
    payment_account_verified = models.BooleanField(default=False)   # for verifying account details


class Meals(models.Model):
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
    meal_cook = models.ForeignKey(Users)  # can further validate that user is indeed a cook..
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

class Orders(models.Model):
    '''
    Maintains order information
    TODO: Payments should not be transferred to cooks immediately, only upon order is filled..some grey area here to figure out
    '''

    order_id = models.AutoField(primary_key=True)
    order_meal = models.ForeignKey(Meals)
    order_user = models.ForeignKey(Users)  # TODO: Check subscriber isn't same as cook...but why?
    order_portions = models.IntegerField(blank=False)  # TODO: Validate order_portions <= available_portions
    order_special_notes = models.TextField(blank=True, default='')
    order_reviewed = models.BooleanField(default=False)
    order_filled = models.BooleanField(default=False)
    order_rated = models.BooleanField(default=False)
    order_total = models.DecimalField(blank=False, decimal_places=2, max_digits=5)
    order_payment_received = models.BooleanField(default=False)
    order_creation_datetime = models.DateTimeField(blank=False, default=timezone.now())
    order_modification_datetime = models.DateTimeField(blank=False, default=timezone.now())

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

    rating_order = models.OneToOneField(Orders)    # Each order can only be rated once../or reviewed..becomes primary key..
    rating_meal = models.ForeignKey(Meals)    # Must be able to link to a meal
    rating_user = models.ForeignKey(Users)    # Must be able to link to a user (TODO: Can't be cook!)

    # Rating on 4 basic dimensions: taste, value, service, punctuality
    rating_value = models.IntegerField(choices=RATING_CHOICES)  # could make this comma seperated integers, but have to do more validation
    rating_service = models.IntegerField(choices=RATING_CHOICES)
    rating_time = models.IntegerField(choices=RATING_CHOICES)
    rating_taste = models.IntegerField(choices=RATING_CHOICES)