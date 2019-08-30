from rest_framework import serializers

from pet.models import Pet, Breed, Picture


class PictureSerializer(serializers.ModelSerializer):
    alt = serializers.CharField(source='title')
    url = serializers.ImageField(source='image')

    class Meta:
        model = Picture
        fields = (
            'id',
            'alt',
            'url',
        )


class PetSerializer(serializers.ModelSerializer):
    breed = serializers.CharField()
    mainPicture = PictureSerializer(source='picture')
    pictures = PictureSerializer(many=True)
    dateAdded = serializers.CharField(source='date_added')
    dateChanged = serializers.CharField(source='date_changed')

    class Meta:
        model = Pet
        fields = (
            'id',
            'slug',
            'name',
            'sex',
            'description',
            'breed',
            'kind',
            'mainPicture',
            'pictures',
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
