import pytest
from model_mommy import mommy
from rest_framework.test import APIClient


@pytest.fixture
def public_client():
    client = APIClient()
    return client


@pytest.fixture
def pet(breed):
    return mommy.make(
        'pet.Pet',
        name='moacir',
        breed=breed,
    )


@pytest.fixture
def pet_moacir(breed_pug):
    return mommy.make(
        'pet.Pet',
        name='Moacir',
        slug='moacir',
        sex='female',
        breed=breed_pug,
        description='Moacir is a funny pug!'
    )


@pytest.fixture
def pet_male(breed):
    return mommy.make(
        'pet.Pet',
        sex='male',
        breed=breed,
    )


@pytest.fixture
def pet_female(breed):
    return mommy.make(
        'pet.Pet',
        sex='female',
        breed=breed,
    )


@pytest.fixture
def pet_pug(breed_pug):
    return mommy.make(
        'pet.Pet',
        breed=breed_pug,
    )


@pytest.fixture
def pet_boxer(breed_boxer):
    return mommy.make(
        'pet.Pet',
        breed=breed_boxer,
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
def breed_boxer():
    return mommy.make(
        'pet.Breed',
        kind='dog',
        name='Boxer',
        slug='boxer',
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


@pytest.fixture
def comment(announcement):
    return mommy.make(
        'announcement.Comment',
        announcement=announcement,
    )
