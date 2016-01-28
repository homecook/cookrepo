"""cookdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
""""""cookdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings # needed to check for debug status etc..
from users import views as user_views
from meals import views as meal_views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'meals', meal_views.MealViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', user_views.test_home, name='home'),
    url(r'^user.details/(?P<user_id>\d+)$', user_views.test_user_details, name='user_details'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cook.meals/(?P<cook_id>\d+)$', meal_views.cook_meals_view, name='meals_by_cook'),
    url(r'^meal.create/', meal_views.meal_detail, name='create_meal'),
    url(r'^meal.details/(?P<meal_id>\d+)$', meal_views.meal_detail, name='meal_detail')
]


