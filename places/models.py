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
    position = models.PositiveIntegerField("Позиция", default=1)

    def __str__(self):
        return f"Изображение для {self.place.title}"

    def save(self, *args, **kwargs):
        if not self.pk:
            last = PlaceImage.objects.filter(place=self.place).order_by('-position').first()
            self.position = last.position + 1 if last else 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pos = self.position
        place_id = self.place_id
        super().delete(*args, **kwargs)
        PlaceImage.objects.filter(place_id=place_id, position__gt=pos).update(position=models.F('position') - 1)

    class Meta:
        ordering = ["position"]
        verbose_name = "Изображение места"
        verbose_name_plural = "Изображения мест"


@receiver(post_delete, sender=PlaceImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)
