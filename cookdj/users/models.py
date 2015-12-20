from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
import datetime

class User(models.Model):
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

    payment_user = models.ForeignKey(User)
    payment_default_pay = models.BooleanField(default=False)
    payment_default_receive = models.BooleanField(default=False)
    payment_account_type = models.CharField(choices=ACCOUNT_CHOICES, max_length=240)
    payment_account_info = models.CommaSeparatedIntegerField(max_length=240)   # ACCOUNT_NUMBER, SECURITY_CODE OR #ACCOUNT_NUMBER OR ACCOUNT_NUMBER, BRANCH_NUMBER
    payment_account_expiry = models.CommaSeparatedIntegerField(max_length=7) # YYYY,MM (e.g. 2018,05)
    payment_account_verified = models.BooleanField(default=False)   # for verifying account details

