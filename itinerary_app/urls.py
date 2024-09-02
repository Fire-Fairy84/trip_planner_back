from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('itineraries', views.ItineraryView, basename='itinerary')
router.register('itinerary-details', views.ItineraryDetailsView, basename='itinerary-details')
router.register('favorites', views.FavoritesView, basename='favorites')


urlpatterns = [

    path('', include(router.urls))
]