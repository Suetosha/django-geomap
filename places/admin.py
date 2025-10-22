from django.contrib import admin
from django import forms

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
    fields = ('image', 'position')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    search_fields = ('title',)
    inlines = [PlaceImageInline]
