import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestPetView:

    def test_pet_list_response(self, client):
        url = reverse('pet-list')
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK

    def test_pet_detail_response(self, client, pet):
        url = reverse(f'pet-detail', kwargs={'pk': pet.pk})
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestBreedView:

    def test_breed_list_response(self, client):
        url = reverse('breed-list')
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK

    def test_breed_detail_response(self, client, breed):
        url = reverse(f'breed-detail', kwargs={'pk': breed.pk})
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestAnnouncementView:

    def test_announcement_list_response(self, client):
        url = reverse('announcement-list')
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK

    def test_announcement_detail_response(self, client, announcement):
        url = reverse(f'announcement-detail', kwargs={'pk': announcement.pk})
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestCityView:

    def test_city_list_response(self, client):
        url = reverse('city-list')
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK

    def test_city_detail_response(self, client, city):
        url = reverse(f'city-detail', kwargs={'pk': city.pk})
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestUserView:

    def test_user_list_response(self, client):
        url = reverse('user-list')
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK

    def test_user_detail_response(self, client, user):
        url = reverse(f'user-detail', kwargs={'pk': user.pk})
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestBannerView:

    def test_banner_list_response(self, client):
        url = reverse('banner-list')
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK

    def test_banner_detail_response(self, client, banner):
        url = reverse(f'banner-detail', kwargs={'pk': banner.pk})
        response = client.get(url, secure=True)
        assert response.status_code == status.HTTP_200_OK
