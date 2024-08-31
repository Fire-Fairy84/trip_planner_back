import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
class TestRegisterView:
    def setup_method(self):
        self.client = APIClient()
        self.register_url = reverse('register')  # Obtiene la URL de la ruta 'register'

    def test_register_user_success(self):
        payload = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.register_url, payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.count() == 1
        assert User.objects.get().username == 'testuser'

@pytest.mark.django_db
class TestLogoutView:
    def setup_method(self):
        self.client = APIClient()
        self.logout_url = reverse('logout')
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token, _ = Token.objects.get_or_create(user=self.user)

    def test_logout_user_success(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.post(self.logout_url)
        assert response.status_code == status.HTTP_200_OK
        assert not Token.objects.filter(user=self.user).exists()

    def test_logout_user_without_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token invalidtoken')
        response = self.client.post(self.logout_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data['detail'] == 'Invalid token.'  # Ajusta el mensaje según tu implementación
