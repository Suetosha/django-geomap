from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Place(models.Model):
    placeId = models.AutoField(primary_key=True)
    title = models.CharField("Название", max_length=200)
    description_short = models.TextField("Короткое описание", max_length=400)
    description_long = models.TextField("Подробное описание", max_length=5000)
    lng = models.FloatField("Долгота")
    lat = models.FloatField("Широта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="images/")

    def __str__(self):
        return f"Изображение для {self.place.title}"

    class Meta:
        verbose_name = "Изображение места"
        verbose_name_plural = "Изображения мест"


@receiver(post_delete, sender=PlaceImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)
