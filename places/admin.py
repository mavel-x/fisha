from django.contrib import admin
from adminsortable2.admin import SortableAdminBase, SortableTabularInline

from .models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    ordering = ['position']
    readonly_fields = ["preview"]
    fields = ('image', 'preview', 'position')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        PlaceImageInline
    ]
    search_fields = ['title']


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    fields = ('image', 'preview', 'position')
