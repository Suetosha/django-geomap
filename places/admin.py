from ckeditor.widgets import CKEditorWidget
from django import forms
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


class PlaceAdminForm(forms.ModelForm):
    description_long = forms.CharField(label="Подробное описание", widget=CKEditorWidget())

    class Meta:
        model = Place
        fields = '__all__'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    form = PlaceAdminForm
    list_display = ('title', 'lng', 'lat')
    search_fields = ('title',)
    inlines = [PlaceImageInline]
