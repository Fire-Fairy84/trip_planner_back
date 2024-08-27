from django.urls import include, path
from rest_framework import routers
from itinerary_app import views

# Para que acceda a los métodos de views
router = routers.DefaultRouter()
router.register('itineraries', views.ItineraryView, basename='itinerary')
router.register('itinerary-details', views.ItineraryDetailsView, basename='itinerary-details')


# Aquí definimos la estructura de la url para cargarla al enrutador
urlpatterns = [
    # Nombre de la ruta de entrada api
    path('', include(router.urls))
]