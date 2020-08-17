from django.urls import include, path
from rest_framework.routers import DefaultRouter

# Views
from profiles import views

#router = DefaultRouter()
#router.register(r'profiles', views.PlansView.as_view(), basename='profiles')

urlpatterns = [
    # path('', include(router.urls)),
    path('profiles/', views.PlansView.as_view(), name='profiles'),
]
