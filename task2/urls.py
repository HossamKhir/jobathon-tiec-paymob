#! /usr/bin/env python
from django.urls import path, include
from rest_framework import routers
from task2 import views


router = routers.DefaultRouter()
router.register(r"persons", views.PersonViewSet)


urlpatterns = [
    path("persons/", include(router.urls)),
]
