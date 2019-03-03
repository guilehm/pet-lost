from django.contrib import admin

from pet.models import Breed, Pet


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind')
    list_filter = ('kind', 'date_added')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name', 'kind')}


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'kind', 'breed', 'lost_date')
    list_filter = ('status', 'lost_date', 'kind', 'breed')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name', 'kind')}
