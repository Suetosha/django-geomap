from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from .models import Place, PlaceImage

class PlaceImageInline(SortableStackedInline):
    model = PlaceImage
    extra = 1
    fields = ('image', 'preview', 'position')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.pk and obj.image:
            return format_html(
                '<img src="{}" style="max-height:150px; max-width:170px; object-fit:contain;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    search_fields = ('title',)
    inlines = [PlaceImageInline]