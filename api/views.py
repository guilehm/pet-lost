from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serializers import PetSerializer
from pet.models import Pet


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (AllowAny,)
