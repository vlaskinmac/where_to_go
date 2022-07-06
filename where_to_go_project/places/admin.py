from django.contrib import admin
from django.utils.html import format_html

from . models import Place, PlaceImage


class ImageAdmin(admin.TabularInline):

    model = PlaceImage
    readonly_fields = ("preview_image", 'id_image')

    fields = ('image', 'preview_image', 'id_image',)

    def preview_image(self, obj):
        return format_html('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height='200px',
        )
        )

    preview_image.short_description = "Фотки"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [
        ImageAdmin,
    ]
