from django.urls import include, path
from rest_framework import routers
from accommodation_app import views


router = routers.DefaultRouter()
router.register('accommodation_app', views.AccommodationView, 'accommodation_app')


urlpatterns = [

    path('', include(router.urls))
]
