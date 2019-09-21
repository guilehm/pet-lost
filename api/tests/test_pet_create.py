import pytest
from django.urls import reverse
from rest_framework import status

from pet.models import Pet


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

    @pytest.fixture
    def pet_creation_payload(self, user, breed_boxer):
        return {
            "user": user.id,
            "name": "Joacir",
            "sex": "female",
            "kind": "dog",
            "breed": "boxer",
            "description": "Doggo ipsum wow such tempt borkdrive pats fat boi",
        }

    @pytest.fixture
    def pet_creation_payload_with_slug(self, pet_creation_payload):
        payload = deepcopy(pet_creation_payload)
        payload['slug'] = 'fake-slug'
        return payload

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

    def test_create_pet(
            self,
            pets_endpoint,
            public_client,
            pet_creation_payload,
            user,
            breed_boxer,
    ):
        response = public_client.post(
            pets_endpoint, data=pet_creation_payload, format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED
        pet = Pet.objects.get(id=response.data['id'])
        assert pet.user == user
        assert pet.breed == breed_boxer
        assert pet.slug == f'joacir-dog-boxer-{str(response.data["id"])[:5]}'
