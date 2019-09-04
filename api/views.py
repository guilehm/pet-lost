from django.contrib.postgres.search import SearchVector
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.filters import AnnouncementFilterSet, PetFilterSet
from api.serializers import (
    PetSerializer, BreedSerializer, AnnouncementSerializer, CitySerializer, UserSerializer,
    BannerSerializer
)
from location.models import City
from pet.models import Pet, Breed, Announcement
from users.models import User
from web.models import Banner


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (AllowAny,)
    filterset_class = PetFilterSet

    def get_queryset(self):
        if self.action_map.get('get') == 'list':
            pets = Pet.objects.all()
            search_query = self.request.GET.get('search')
            if search_query:
                pets = pets.annotate(
                    search=SearchVector(
                        'name',
                        'description',
                    )
                ).filter(search=search_query)
            return pets
        return Pet.objects.all()


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (AllowAny,)


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (AllowAny,)
    filterset_class = AnnouncementFilterSet

    def get_queryset(self):
        if self.action_map.get('get') == 'list':
            announcements = Announcement.objects.all()
            search_query = self.request.GET.get('search')
            if search_query:
                announcements = announcements.annotate(
                    search=SearchVector(
                        'description',
                    )
                ).filter(search=search_query)
            return announcements
        return Announcement.objects.all()


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = (AllowAny,)
