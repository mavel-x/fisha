from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminBase, SortableTabularInline

from .models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    readonly_fields = ['preview']
    fields = ('image', 'preview', 'position')

    def preview(self, obj):
        return format_html(
            '<img src="{url}" height={height} />',
            url=obj.image.url,
            height=min(obj.image.height, 200),
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceImageInline
    ]
    search_fields = ['title']


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    fields = ('image', 'position')
    ordering = ('place__title', 'position')
