from django.contrib import admin

from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lat', 'lng')
    search_fields = ('title',)
    inlines = [PlaceImageInline]
