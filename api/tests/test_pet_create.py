import pytest
from django.urls import reverse
from pet.models import Pet
from rest_framework import status


@pytest.mark.django_db
class TestPetCreation:

    @pytest.fixture
    def pets_endpoint(self):
        return reverse('pet-list')

    @pytest.fixture
    def minimal_pet_creation_payload(self, user, breed_pug):
        return {
            "sex": "male",
            "breed": "pug",
            "name": "Adalberto",
            "user": user.id,
        }

    def test_create_pet_minimal_data(
            self,
            pets_endpoint,
            public_client,
            minimal_pet_creation_payload,
            user,
            breed_pug,
    ):
        response = public_client.post(
            pets_endpoint, data=minimal_pet_creation_payload, format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
        pet = Pet.objects.get(id=response.data['id'])
        assert pet.user == user
        assert pet.breed == breed_pug

