import pytest
from model_mommy import mommy
from rest_framework.test import APIClient


@pytest.fixture
def public_client():
    client = APIClient()
    return client


@pytest.fixture
def pet():
    return mommy.make(
        'pet.Pet',
    )


@pytest.fixture
def pet_male():
    return mommy.make(
        'pet.Pet',
        sex='male',
    )


@pytest.fixture
def pet_female():
    return mommy.make(
        'pet.Pet',
        sex='female',
    )


@pytest.fixture
def breed_pug():
    return mommy.make(
        'pet.Breed',
        kind='dog',
        name='Pug',
        slug='pug',
    )
