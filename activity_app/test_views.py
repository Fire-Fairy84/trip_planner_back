import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from activity_app.models import Activity
from destination_app.models import Destination

@pytest.mark.django_db
class TestActivityView:

    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def destination(self):
        return Destination.objects.create(name='Paris', description='The city of light', country='France')

    @pytest.fixture
    def activity_data(self, destination):
        return {
            'name': 'Eiffel Tower Tour',
            'type': 'cultural',
            'description': 'A guided tour of the Eiffel Tower.',
            'estimated_price': 100.00,
            'destination': destination.id
        }

    def test_create_activity(self, client, destination):
        url = reverse('activity_app-list')
        activity_data = {
            'name': 'Eiffel Tower Tour',
            'type': 'cultural',
            'description': 'A guided tour of the Eiffel Tower.',
            'estimated_price': 100.00,
            'destination': destination.id
        }
        response = client.post(url, activity_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Activity.objects.count() == 1
        assert Activity.objects.get().name == activity_data['name']

    def test_list_activities(self, client, destination):
        Activity.objects.create(
            name='Eiffel Tower Tour',
            type='cultural',
            description='A guided tour of the Eiffel Tower.',
            estimated_price=100.00,
            destination=destination
        )
        url = reverse('activity_app-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_get_activity(self, client, destination):
        activity = Activity.objects.create(
            name='Eiffel Tower Tour',
            type='cultural',
            description='A guided tour of the Eiffel Tower.',
            estimated_price=100.00,
            destination=destination
        )
        url = reverse('activity_app-detail', args=[activity.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == activity.name

    def test_update_activity(self, client, destination):

        activity = Activity.objects.create(
            name='Eiffel Tower Tour',
            type='cultural',
            description='A guided tour of the Eiffel Tower.',
            estimated_price=100.00,
            destination=destination
        )
        url = reverse('activity_app-detail', args=[activity.id])
        updated_data = {
            'name': 'Updated Tour',
            'type': 'adventure',
            'description': 'An updated description of the tour.',
            'estimated_price': 150.00,
            'destination': destination.id
        }
        response = client.patch(url, updated_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        activity.refresh_from_db()
        assert activity.name == updated_data['name']
        assert activity.type == updated_data['type']
        assert activity.description == updated_data['description']
        assert activity.estimated_price == updated_data['estimated_price']

    def test_delete_activity(self, client, destination):
        activity = Activity.objects.create(
            name='Eiffel Tower Tour',
            type='cultural',
            description='A guided tour of the Eiffel Tower.',
            estimated_price=100.00,
            destination=destination
        )
        url = reverse('activity_app-detail', args=[activity.id])
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Activity.objects.count() == 0
