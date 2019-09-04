import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestPetFilterSetBySex:

    @pytest.fixture
    def pet_filter_male_response(self, pet_male, pet_female):
        return {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [make_result_for_pet(pet_male)]
        }

    @pytest.fixture
    def pet_filter_female_response(self, pet_male, pet_female):
        return {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [make_result_for_pet(pet_female)]
        }

    @pytest.fixture
    def pet_filter_wrong_sex_response(self, pet_male, pet_female):
        return {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }

    def test_pet_filter_by_male_sex(self, client, pet_male, pet_female, pet_filter_male_response):
        assert pet_male.sex == 'male'
        assert pet_female.sex == 'female'

        url = f'{reverse("pet-list")}?sex=male'
        response = client.get(url, secure=True)
        assert response.json() == pet_filter_male_response

    def test_pet_filter_by_female_sex(self, client, pet_male, pet_female, pet_filter_female_response):
        assert pet_male.sex == 'male'
        assert pet_female.sex == 'female'

        url = f'{reverse("pet-list")}?sex=female'
        response = client.get(url, secure=True)
        assert response.json() == pet_filter_female_response

    def test_pet_filter_by_wrong_sex(self, client, pet_male, pet_female, pet_filter_wrong_sex_response):
        assert pet_male.sex == 'male'
        assert pet_female.sex == 'female'

        url = f'{reverse("pet-list")}?sex=wrong'
        response = client.get(url, secure=True)
        assert response.json() == pet_filter_wrong_sex_response


@pytest.mark.django_db
class TestPetFilterSetByBreed:

    @pytest.fixture
    def pet_filter_breed_pug_response(self, pet_pug, pet_boxer):
        return {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [make_result_for_pet(pet_pug)]
        }

    @pytest.fixture
    def pet_filter_breed_wrong_name_response(self, pet_pug, pet_boxer, pet, pet_male, pet_female, breed):
        return {
            'breed': [
                "Select a valid choice. That choice is not one of the available choices."
            ]
        }

    def test_pet_filter_by_breed_pug(
            self, client, pet_pug, pet_boxer, pet_filter_breed_pug_response,
    ):
        assert pet_pug.breed.name == 'Pug'
        assert pet_boxer.breed.name == 'Boxer'

        url = f'{reverse("pet-list")}?breed=Pug'
        response = client.get(url, secure=True)
        response = response.json()
        assert response == pet_filter_breed_pug_response
        assert response['results'][0]['breed'] == 'Pug'
        assert len(response['results']) == 1

    def test_pet_filter_by_breed_wrong(self, client, pet_pug, pet_boxer, pet_filter_breed_wrong_name_response):
        assert pet_pug.breed.name == 'Pug'
        assert pet_boxer.breed.name == 'Boxer'

        url = f'{reverse("pet-list")}?breed=Wrong'
        response = client.get(url, secure=True)
        assert response.json() == pet_filter_breed_wrong_name_response


def make_result_for_pet(pet):
    if pet:
        return {
            'id': str(pet.id),
            'slug': pet.slug,
            'name': pet.name,
            'sex': pet.sex,
            'description': pet.description,
            'breed': pet.breed.name,
            'kind': pet.kind,
            'mainPicture': None,
            'pictures': [],
            'announcements': [],
            'dateAdded': str(pet.date_added),
            'dateChanged': str(pet.date_changed),
        }
