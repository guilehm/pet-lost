from rest_framework import serializers

from announcement.models import Announcement, Comment
from location.models import City
from pet.models import Breed, Pet, Picture
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


class CommentSerializer(serializers.ModelSerializer):
    dateAdded = serializers.CharField(source='date_added', read_only=True)
    dateChanged = serializers.CharField(source='date_changed', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'announcement',
            'user',
            'deleted',
            'description',
            'dateAdded',
            'dateChanged',
        )


class AnnouncementSerializer(serializers.ModelSerializer):
    rescuedDate = serializers.CharField(source='rescued_date')
    lastSeenDistrict = serializers.CharField(source='last_seen_district')
    lastSeenCity = serializers.CharField(source='last_seen_city')
    lostDate = serializers.DateField(source='lost_date')
    foundDate = serializers.DateField(source='found_date')
    dateAdded = serializers.CharField(source='date_added', read_only=True)
    dateChanged = serializers.CharField(source='date_changed', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

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
            'comments',
            'dateAdded',
            'dateChanged',
        )


class PetSerializer(serializers.ModelSerializer):
    announcements = AnnouncementSerializer(many=True, read_only=True)
    slug = serializers.SlugField(read_only=True)
    mainPicture = PictureSerializer(source='picture')
    pictures = PictureSerializer(many=True)
    dateAdded = serializers.CharField(source='date_added', read_only=True)
    dateChanged = serializers.CharField(source='date_changed', read_only=True)
    user = serializers.CharField(write_only=True)

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
            'announcements',
            'user',
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
    pets = PetSerializer(many=True, read_only=True)
    city = CitySerializer(read_only=True)
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    fullName = serializers.CharField(source='get_full_name')
    postalCode = serializers.CharField(source='postal_code')
    profilePicture = serializers.ImageField(source='profile_picture')
    orgName = serializers.CharField(source='org_name')
    addressData = serializers.CharField(source='get_address_data')
    shareEmail = serializers.BooleanField(source='share_email')
    sharePhone = serializers.BooleanField(source='share_phone')
    phoneNumber = serializers.CharField(source='phone_number')
    mobilePhoneNumber = serializers.CharField(source='mobile_phone_number')
    urlFacebookProfile = serializers.URLField(source='url_facebook_profile')
    urlFacebookPage = serializers.URLField(source='url_facebook_page')
    urlTwitter = serializers.URLField(source='url_twitter')
    urlInstagram = serializers.URLField(source='url_instagram')
    superUser = serializers.BooleanField(source='is_superuser')
    dateJoined = serializers.CharField(source='date_joined')
    lastLogin = serializers.CharField(source='last_login')

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
