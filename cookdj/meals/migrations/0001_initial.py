# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 01:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('meal_id', models.AutoField(primary_key=True, serialize=False)),
                ('meal_name', models.CharField(max_length=150)),
                ('meal_description', models.TextField(blank=True, default='')),
                ('meal_available_date', models.DateField()),
                ('meal_available_time', models.TimeField()),
                ('meal_expiry_date', models.DateField()),
                ('meal_expiry_time', models.TimeField()),
                ('meal_price', models.DecimalField(decimal_places=0, max_digits=2)),
                ('meal_servings', models.IntegerField()),
                ('meal_gluent_free', models.BooleanField(default=False)),
                ('meal_nut_free', models.BooleanField(default=False)),
                ('meal_lactose_free', models.BooleanField(default=False)),
                ('meal_spice_level', models.CharField(choices=[('L', 'Mild'), ('M', 'Medium'), ('H', 'Hot')], max_length=240)),
                ('meal_cusine', models.CharField(choices=[('Indian', 'Indian'), ('Spanish', 'Spanish'), ('Italian', 'Italian'), ('European', 'European'), ('American', 'American'), ('Asian', 'Asian'), ('Other', 'Other')], default='Other', max_length=240)),
                ('meal_mealtype', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Brunch', 'Brunch'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Dessert', 'Dessert'), ('Other', 'Other')], default='Other', max_length=240)),
                ('meal_creation_datetime', models.DateTimeField(default=datetime.datetime(2015, 12, 20, 1, 14, 50, 87532, tzinfo=utc))),
                ('meal_modification_datetime', models.DateTimeField(default=datetime.datetime(2015, 12, 20, 1, 14, 50, 87583, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='MealRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField(choices=[(1, 'Terrible'), (2, 'Meh'), (3, 'Good'), (4, 'Nice!'), (5, 'Como Casa!!!'), (0, 'Unrated/NA')])),
                ('rating_service', models.IntegerField(choices=[(1, 'Terrible'), (2, 'Meh'), (3, 'Good'), (4, 'Nice!'), (5, 'Como Casa!!!'), (0, 'Unrated/NA')])),
                ('rating_time', models.IntegerField(choices=[(1, 'Terrible'), (2, 'Meh'), (3, 'Good'), (4, 'Nice!'), (5, 'Como Casa!!!'), (0, 'Unrated/NA')])),
                ('rating_taste', models.IntegerField(choices=[(1, 'Terrible'), (2, 'Meh'), (3, 'Good'), (4, 'Nice!'), (5, 'Como Casa!!!'), (0, 'Unrated/NA')])),
                ('rating_meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Meal')),
            ],
        ),
    ]
