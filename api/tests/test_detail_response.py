import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestPetDetail:

    @pytest.fixture
    def pet_detail_response(self, pet_moacir):
        return {
            "id": "0d91d3b3-0543-46bc-a053-4f457385c803",
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
        url = reverse(f'pet-detail', kwargs={'slug': pet_moacir.slug})
        response = client.get(url, secure=True)
        assert response.json() == pet_detail_response


@pytest.mark.django_db
class TestAnnouncementDetail:

    @pytest.fixture
    def announcement_detail_response(self, announcement):
        return {
            "id": announcement.id,
            "active": True,
            "pet": "0d91d3b3-0543-46bc-a053-4f457385c803",
            "situation": "lost",
            "description": "She got lost somewhere",
            "rescued": False,
            "rescuedDate": None,
            "lastSeenCity": "São Paulo",
            "lastSeenDistrict": "Center",
            "lostDate": "2019-09-03",
            "foundDate": None,
            "comments": [],
            "dateAdded": str(announcement.date_added),
            "dateChanged": str(announcement.date_changed)
        }

    def test_announcement_detail_response(self, client, announcement, announcement_detail_response):
        url = reverse(f'announcement-detail', kwargs={'pk': announcement.pk})
        response = client.get(url, secure=True)
        assert response.json() == announcement_detail_response
