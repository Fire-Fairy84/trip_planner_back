import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from accommodation_app.models import Accommodation
from destination_app.models import Destination


@pytest.mark.django_db
class TestAccommodationView:
    def setup_method(self):
        self.client = APIClient()

        self.destination = Destination.objects.create(
            name='Test Destination',
            description='Test description',
            country='Test Country'
        )

        self.url = reverse('accommodation_app-list')
        self.accommodation_url = lambda pk: reverse('accommodation_app-detail', args=[pk])

    def test_create_accommodation(self):
        data = {
            'name': 'Test Hotel',
            'type': 'hotel',
            'address': '123 Test St',
            'contact': '123-456-7890',
            'estimated_price': '100.00',
            'destination': self.destination.id
        }
        response = self.client.post(self.url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Accommodation.objects.count() == 1
        assert Accommodation.objects.get().name == 'Test Hotel'

    def test_list_accommodations(self):
        Accommodation.objects.create(
            name='Test Hostel',
            type='hostel',
            address='456 Test Ave',
            contact='098-765-4321',
            estimated_price='50.00',
            destination=self.destination
        )
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['name'] == 'Test Hostel'

    def test_get_accommodation(self):
        accommodation = Accommodation.objects.create(
            name='Test BnB',
            type='bnb',
            address='789 Test Blvd',
            contact='567-890-1234',
            estimated_price='75.00',
            destination=self.destination
        )
        response = self.client.get(self.accommodation_url(accommodation.id))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Test BnB'

    def test_update_accommodation(self):

        accommodation = Accommodation.objects.create(
            name='Test Camping',
            type='camping',
            address='101 Test Road',
            contact='678-901-2345',
            estimated_price='30.00',
            destination=self.destination
        )
        data = {
            'name': 'Updated Camping',
            'type': 'camping',
            'address': '101 Updated Road',
            'contact': '678-901-2346',
            'estimated_price': '35.00',
            'destination': self.destination.id
        }
        response = self.client.put(self.accommodation_url(accommodation.id), data, format='json')
        assert response.status_code == status.HTTP_200_OK
        accommodation.refresh_from_db()
        assert accommodation.name == 'Updated Camping'

    def test_delete_accommodation(self):
        accommodation = Accommodation.objects.create(
            name='Test Other',
            type='other',
            address='202 Test Lane',
            contact='789-012-3456',
            estimated_price='20.00',
            destination=self.destination
        )
        response = self.client.delete(self.accommodation_url(accommodation.id))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Accommodation.objects.count() == 0
