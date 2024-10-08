from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField("Название", max_length=150)
    slug = models.SlugField("Слаг", max_length=150, unique=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("menu:menu", kwargs={"menu_slug": self.slug})
