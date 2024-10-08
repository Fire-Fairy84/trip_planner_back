from django.contrib import admin
from itinerary_app.models import Itinerary, ItineraryDetails, Favorites



@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('description', 'duration', 'destination', 'created_at')


@admin.register(ItineraryDetails)
class ItineraryDetailsAdmin(admin.ModelAdmin):
    list_display = ('itinerary', 'day', 'accommodation', 'activity', 'description')


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'itinerary', 'saved_date')