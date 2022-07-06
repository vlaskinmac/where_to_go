from django.contrib import admin

from . models import Place, PlaceImage


class ImageAdmin(admin.TabularInline):
    list_display = ('id_image', 'title',)
    search_fields = ('title',)
    ordering = ('id_image',)
    model = PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [
        ImageAdmin,
    ]