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
        name='moacir',
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
def breed():
    return mommy.make(
        'pet.Breed',
    )


@pytest.fixture
def breed_pug():
    return mommy.make(
        'pet.Breed',
        kind='dog',
        name='Pug',
        slug='pug',
    )


@pytest.fixture
def announcement(pet):
    return mommy.make(
        'announcement.Announcement',
        pet=pet,
        lost_date='2019-09-03',
    )


@pytest.fixture
def city():
    return mommy.make(
        'location.City',
    )


@pytest.fixture
def user():
    return mommy.make(
        'users.User',
    )


@pytest.fixture
def banner():
    return mommy.make(
        'web.Banner',
    )
