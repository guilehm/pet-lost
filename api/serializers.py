from rest_framework import serializers

from pet.models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            'id',
            'slug',
            'name',
            'sex',
            'kind',
            'breed',
            'picture',
            'description',
            'date_added',
            'date_changed',
        )
