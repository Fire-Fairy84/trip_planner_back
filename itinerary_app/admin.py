from django.contrib import admin
from itinerary_app.models import Itinerary, ItineraryDetails


# # Register your models here.
#
# admin.site.register(Itinerary, ItineraryDetails)

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('description', 'duration', 'destination', 'created_at')


@admin.register(ItineraryDetails)
class ItineraryDetailsAdmin(admin.ModelAdmin):
    list_display = ('itinerary', 'day', 'accommodation', 'activity')
