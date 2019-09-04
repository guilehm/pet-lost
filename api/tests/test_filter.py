import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestPetFilterSetBySex:

    def make_result_for_pet(self, pet):
        if pet:
            return {
                'id': str(pet.id),
                'slug': pet.slug,
                'name': pet.name,
                'sex': pet.sex,
                'description': pet.description,
                'breed': pet.breed,
                'kind': pet.kind,
                'mainPicture': None,
                'pictures': [],
                'announcements': [],
                'dateAdded': str(pet.date_added),
                'dateChanged': str(pet.date_changed),
            }

    @pytest.fixture
    def pet_filter_male_response(self, pet_male, pet_female):
        return {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [self.make_result_for_pet(pet_male)]
        }

    @pytest.fixture
    def pet_filter_female_response(self, pet_male, pet_female):
        return {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [self.make_result_for_pet(pet_female)]
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
        response = client.get(url)
        assert response.json() == pet_filter_male_response

    def test_pet_filter_by_female_sex(self, client, pet_male, pet_female, pet_filter_female_response):
        assert pet_male.sex == 'male'
        assert pet_female.sex == 'female'

        url = f'{reverse("pet-list")}?sex=female'
        response = client.get(url)
        assert response.json() == pet_filter_female_response

    def test_pet_filter_by_wrong_sex(self, client, pet_male, pet_female, pet_filter_wrong_sex_response):
        assert pet_male.sex == 'male'
        assert pet_female.sex == 'female'

        url = f'{reverse("pet-list")}?sex=wrong'
        response = client.get(url)
        assert response.json() == pet_filter_wrong_sex_response
