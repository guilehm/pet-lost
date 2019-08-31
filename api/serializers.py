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


class AnnouncementSerializer(serializers.ModelSerializer):
    rescuedDate = serializers.CharField(source='rescued_date')
    lastSeenDistrict = serializers.CharField(source='last_seen_district')
    lastSeenCity = serializers.CharField(source='last_seen_city')
    lostDate = serializers.DateField(source='lost_date')
    foundDate = serializers.DateField(source='found_date')
    dateAdded = serializers.CharField(source='date_added')
    dateChanged = serializers.CharField(source='date_changed')

    class Meta:
        model = Announcement
        fields = (
            'id',
            'active',
            'pet',
            'situation',
            'description',
            'rescued',
            'rescuedDate',
            'lastSeenCity',
            'lastSeenDistrict',
            'lostDate',
            'foundDate',
            'dateAdded',
            'dateChanged',
        )


class PetSerializer(serializers.ModelSerializer):
    announcements = AnnouncementSerializer(many=True)
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


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name', 'state')
