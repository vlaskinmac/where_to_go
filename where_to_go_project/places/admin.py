from django.contrib import admin

from . models import Place, PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(PlaceImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id_image', 'title',)
    search_fields = ('title',)
    ordering = ('id_image',)