import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestPetDetail:

    @pytest.fixture
    def pet_detail_response(self, pet_moacir):
        return {
            "id": str(pet_moacir.id),
            "slug": "moacir",
            "name": "Moacir",
            "sex": "female",
            "description": "Moacir is a funny pug!",
            "breed": "Pug",
            "kind": "dog",
            "mainPicture": None,
            "pictures": [],
            "announcements": [],
            "dateAdded": str(pet_moacir.date_added),
            "dateChanged": str(pet_moacir.date_changed)
        }

    def test_pet_response(self, client, pet_moacir, pet_detail_response):
        url = reverse(f'pet-detail', kwargs={'pk': pet_moacir.pk})
        response = client.get(url, secure=True)
        assert response.json() == pet_detail_response
