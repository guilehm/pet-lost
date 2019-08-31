from rest_framework import serializers

from pet.models import Pet, Breed, Picture
from announcement.models import Announcement
from location.models import City
from users.models import User
from web.models import Banner


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


class BannerSerializer(serializers.ModelSerializer):
    buttonOne = serializers.CharField(source='button_one')
    buttonTwo = serializers.CharField(source='button_two')
    buttonOneLink = serializers.CharField(source='button_one_link')
    buttonTwoLink = serializers.CharField(source='button_two_link')

    class Meta:
        model = Banner
        fields = (
            'title',
            'subtitle',
            'slug',
            'active',
            'picture',
            'buttonOne',
            'buttonOneLink',
            'buttonTwo',
            'buttonTwoLink',
        )


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    fullName = serializers.CharField(source='get_full_name')
    dateJoined = serializers.CharField(source='date_joined')
    lastLogin = serializers.CharField(source='last_login')
    city = CitySerializer()
    postalCode = serializers.CharField(source='postal_code')
    profilePicture = serializers.ImageField(source='profile_picture')
    orgName = serializers.CharField(source='org_name')
    addressData = serializers.CharField(source='get_address_data')

    superUser = serializers.BooleanField(source='is_superuser')
    shareEmail = serializers.BooleanField(source='share_email')
    sharePhone = serializers.BooleanField(source='share_phone')

    phoneNumber = serializers.CharField(source='phone_number')
    mobilePhoneNumber = serializers.CharField(source='mobile_phone_number')

    urlFacebookProfile = serializers.URLField(source='url_facebook_profile')
    urlFacebookPage = serializers.URLField(source='url_facebook_page')
    urlTwitter = serializers.URLField(source='url_twitter')
    urlInstagram = serializers.URLField(source='url_instagram')

    pets = PetSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'firstName',
            'lastName',
            'fullName',
            'email',
            'address',
            'number',
            'complement',
            'district',
            'city',
            'addressData',
            'orgName',
            'profilePicture',
            'phoneNumber',
            'mobilePhoneNumber',
            'urlFacebookProfile',
            'urlFacebookPage',
            'urlTwitter',
            'urlInstagram',
            'shareEmail',
            'sharePhone',
            'description',
            'postalCode',
            'superUser',
            'lastLogin',
            'dateJoined',
            'pets',
        )
