"""Extras URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from extras import views

router = DefaultRouter()
router.register(r'extra', views.ExtraViewSet, basename='extra')

urlpatterns = [
    path('', include(router.urls))
]