from django.contrib import admin
from django import forms
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInlineForm(forms.ModelForm):
    class Meta:
        model = PlaceImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['position'].initial = None


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    form = PlaceImageInlineForm
    extra = 1
    fields = ('image', 'preview', 'position')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:150px; max-width:170px; object-fit:contain;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    search_fields = ('title',)
    inlines = [PlaceImageInline]
