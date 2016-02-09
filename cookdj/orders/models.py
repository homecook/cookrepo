from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
import datetime

class Order(models.Model):
    '''
    Maintains order information
    TODO: Payments should not be transferred to cooks immediately, only upon order is filled..some grey area here to figure out
    '''

    order_id = models.AutoField(primary_key=True)
    order_meal = models.ForeignKey('meals.Meal', on_delete=models.CASCADE, related_name='orders')   # related_name allows reverse relationship/link from meal object
    order_user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders')  # TODO: Check subscriber isn't same as cook...but why?
    order_portions = models.IntegerField(blank=False)  # TODO: Validate order_portions <= available_portions
    # order_special_notes = models.TextField(blank=True, default='')
    order_reviewed = models.BooleanField(default=False)
    order_filled = models.BooleanField(default=False)
    order_rated = models.BooleanField(default=False)
    order_total = models.DecimalField(blank=False, decimal_places=2, max_digits=5)
    order_payment_received = models.BooleanField(default=False)
    order_creation_datetime = models.DateTimeField(blank=False, default=timezone.now())
    order_modification_datetime = models.DateTimeField(blank=False, default=timezone.now())

    def __str__(self):
        return str(self.order_id) + ': ' + str(self.order_meal) + ' by ' + str(self.order_user) + ' (' + str(self.order_portions) + ' portions)'