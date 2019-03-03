from django.contrib import admin

from pet.models import Breed, Pet, Picture


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind')
    list_filter = ('kind', 'date_added')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name', 'kind')}


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'situation', 'rescued', 'kind', 'breed', 'lost_date', 'found_date'
    )
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name', 'kind', 'situation')}
    list_filter = (
        'situation',
        'rescued',
        'sex',
        'kind',
        'rescued_date',
        'lost_date',
        'found_date',
        'breed',
    )


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'date_added')
    list_filter = ('date_added', 'date_changed')
