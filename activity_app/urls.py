from django.urls import include, path
from rest_framework import routers
from activity_app import views


router = routers.DefaultRouter()
router.register('activity_app', views.ActivityView, 'activity_app')


urlpatterns = [

    path('', include(router.urls))
]