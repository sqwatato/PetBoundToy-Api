from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'opportunities', views.OpportunityViewSet)
router.register(r'shelters', views.ShelterViewSet)
urlpatterns = [
    path('', include(router.urls)),
]