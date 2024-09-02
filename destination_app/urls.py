from django.urls import include, path
from rest_framework import routers
from destination_app import views


router = routers.DefaultRouter()
router.register('destination_app', views.DestinationView, 'destination_app')


urlpatterns = [

    path('', include(router.urls))
]
