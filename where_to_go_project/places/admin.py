from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from . models import Place, PlaceImage


class ImageAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra: int = 0
    readonly_fields = ["preview_image"]
    fields = ['image', 'preview_image']

    def preview_image(self, obj):
        return format_html('<img src="{url}" height={height} />', url=obj.image.url, height='200px',)
    preview_image.short_description = "Фотки"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageAdmin
    ]

