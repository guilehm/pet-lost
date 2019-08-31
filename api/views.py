from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serializers import PetSerializer, BreedSerializer
from pet.models import Pet, Breed


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (AllowAny,)


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (AllowAny,)


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = (AllowAny,)


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)

