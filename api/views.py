from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

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
    filterset_fields = [
        'name',
        'sex',
        'breed',
        'kind',
    ]


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (AllowAny,)


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (AllowAny,)
    filterset_fields = [
        'active',
        'pet',
        'situation',
        'rescued',
        'rescued_date',
        'last_seen_city',
        'lost_date',
        'found_date',
    ]


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
