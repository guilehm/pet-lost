from rest_framework import serializers

from pet.models import Pet, Breed


class PetSerializer(serializers.ModelSerializer):
    dateAdded = serializers.CharField(source='date_added')
    dateChanged = serializers.CharField(source='date_changed')

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
            'dateAdded',
            'dateChanged',
        )


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = (
            'id',
            'name',
            'kind',
            'slug',
            'description',
        )
