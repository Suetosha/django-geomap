from django.db import models


class Place(models.Model):
    placeId = models.AutoField(primary_key=True)
    title = models.CharField("Название", max_length=200)
    description_short = models.TextField("Короткое описание", max_length=400)
    description_long = models.TextField("Подробное описание", max_length=5000)
    lat = models.FloatField("Широта")
    lng = models.FloatField("Долгота")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="media/")

    def __str__(self):
        return f"Изображение для {self.place.title}"

    class Meta:
        verbose_name = "Изображение места"
        verbose_name_plural = "Изображения мест"
