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
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from users import views as user_views
from meals import views as meal_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'meals', meal_views.MealViewSet)   # basic meal views for retrieve, update, delete, create
router.register(r'users', user_views.UserViewSet)   # basic user views for retrieve, update, delete, create

cooks_meals = meal_views.MealViewSet.as_view({      # detailed route for getting basic meal information for a cook
    'get': 'cooks_meals'    # function user the viewset that this view is mapped to
})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cook.meals/(?P<cook_id>\d+)', cooks_meals, name='cooks_meals'),     # detailed route for cook's meals
    url(r'^', include(router.urls))
]

# Adding url suffix patterns, we allow for alternate formats to be specified in url (like appending .json at end of url)
# urlpatterns = format_suffix_patterns(urlpatterns)