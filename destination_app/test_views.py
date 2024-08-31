import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from destination_app.models import Destination
import warnings
from django.utils.deprecation import RemovedInDjango60Warning

warnings.filterwarnings('ignore', category=RemovedInDjango60Warning)



@pytest.mark.django_db
class TestDestinationView:
    def setup_method(self):
        self.client = APIClient()
        self.destination_list_url = reverse('destination_app-list')

        # Crear un destino para las pruebas
        self.destination = Destination.objects.create(
            name='Test Destination',
            description='A beautiful place.',
            country='Testland'
        )
        self.destination_detail_url = reverse('destination_app-detail', args=[self.destination.id])

    def test_create_destination(self):
        payload = {
            'name': 'New Destination',
            'description': 'A new place to visit.',
            'country': 'Newland'
        }
        response = self.client.post(self.destination_list_url, payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Destination.objects.count() == 2
        assert Destination.objects.get(name='New Destination')

    def test_list_destinations(self):
        response = self.client.get(self.destination_list_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_get_destination(self):
        response = self.client.get(self.destination_detail_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == self.destination.name

    def test_update_destination(self):
        payload = {
            'name': 'Updated Destination',
            'description': 'Updated description.',
            'country': 'Updatedland'
        }
        response = self.client.put(self.destination_detail_url, payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        self.destination.refresh_from_db()
        assert self.destination.name == 'Updated Destination'

    def test_delete_destination(self):
        response = self.client.delete(self.destination_detail_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Destination.objects.count() == 0
