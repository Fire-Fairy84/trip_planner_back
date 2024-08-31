import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from itinerary_app.models import Itinerary, ItineraryDetails, Favorites
from destination_app.models import Destination  # Asegúrate de importar Destination si se usa en las pruebas
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestItineraryView:
    def setup_method(self):
        self.client = APIClient()
        self.itinerary_url = reverse('itinerary-list')
        self.destination = Destination.objects.create(name='Test Destination')
        self.itinerary = Itinerary.objects.create(
            description='Test Itinerary',
            duration=1,
            destination=self.destination
        )

    def test_create_itinerary(self):
        payload = {
            'description': 'New Itinerary',
            'duration': 2,
            'destination': self.destination.id
        }
        response = self.client.post(self.itinerary_url, payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Itinerary.objects.count() == 2

    def test_list_itineraries(self):
        response = self.client.get(self.itinerary_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_itinerary(self):
        response = self.client.get(reverse('itinerary-detail', args=[self.itinerary.id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == 'Test Itinerary'

    def test_update_itinerary(self):
        payload = {
            'description': 'Updated Itinerary',
            'duration': 3,
            'destination': self.destination.id
        }
        response = self.client.put(reverse('itinerary-detail', args=[self.itinerary.id]), payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.itinerary.refresh_from_db()
        assert self.itinerary.description == 'Updated Itinerary'

    def test_delete_itinerary(self):
        response = self.client.delete(reverse('itinerary-detail', args=[self.itinerary.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Itinerary.objects.count() == 0


@pytest.mark.django_db
class TestItineraryDetailsView:
    def setup_method(self):
        self.client = APIClient()
        self.itinerary_details_url = reverse('itinerary-details-list')
        self.destination = Destination.objects.create(name='Test Destination')
        self.itinerary = Itinerary.objects.create(
            description='Test Itinerary',
            duration=1,
            destination=self.destination
        )
        self.itinerary_details = ItineraryDetails.objects.create(
            itinerary=self.itinerary,
            day=1,
            description='Test Itinerary Detail'
        )

    def test_create_itinerary_details(self):
        payload = {
            'itinerary': self.itinerary.id,
            'day': 2,
            'description': 'New Itinerary Detail'
        }
        response = self.client.post(self.itinerary_details_url, payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert ItineraryDetails.objects.count() == 2

    def test_list_itinerary_details(self):
        response = self.client.get(self.itinerary_details_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_itinerary_details(self):
        response = self.client.get(reverse('itinerary-details-detail', args=[self.itinerary_details.id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == 'Test Itinerary Detail'

    def test_update_itinerary_details(self):
        payload = {
            'itinerary': self.itinerary.id,
            'day': 3,
            'description': 'Updated Itinerary Detail'
        }
        response = self.client.put(reverse('itinerary-details-detail', args=[self.itinerary_details.id]), payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.itinerary_details.refresh_from_db()
        assert self.itinerary_details.description == 'Updated Itinerary Detail'

    def test_delete_itinerary_details(self):
        response = self.client.delete(reverse('itinerary-details-detail', args=[self.itinerary_details.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert ItineraryDetails.objects.count() == 0


@pytest.mark.django_db
class TestFavoritesView:
    def setup_method(self):
        self.client = APIClient()
        self.favorites_url = reverse('favorites-list')
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.destination = Destination.objects.create(name='Test Destination')
        self.itinerary = Itinerary.objects.create(
            description='Test Itinerary',
            duration=1,
            destination=self.destination
        )
        self.favorite = Favorites.objects.create(
            user=self.user,
            itinerary=self.itinerary
        )


    def test_list_favorites(self):
        response = self.client.get(self.favorites_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_favorite(self):
        response = self.client.get(reverse('favorites-detail', args=[self.favorite.id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['user'] == self.user.id

    def test_update_favorite(self):
        new_user = User.objects.create_user(username='newuser', password='password123')
        payload = {
            'user': new_user.id,
            'itinerary': self.itinerary.id
        }
        response = self.client.put(reverse('favorites-detail', args=[self.favorite.id]), payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.favorite.refresh_from_db()
        assert self.favorite.user == new_user

    def test_delete_favorite(self):
        response = self.client.delete(reverse('favorites-detail', args=[self.favorite.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Favorites.objects.count() == 0
