from tabnanny import verbose

from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Staff")
    content = models.TextField(verbose_name="Description")
    price = models.FloatField(verbose_name="Price")
    published = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Published")
    rubric = models.ForeignKey("Rubric", null=True, on_delete=models.PROTECT, verbose_name="Rubric")

    class Meta:
        verbose_name_plural = 'Announcements'
        verbose_name = "Announcement"
        ordering = ["-published"]


class Rubric(models.Model):
     name = models.CharField(max_length=20, db_index=True, verbose_name="Title")

     def __str__(self):
         return self.name

     class Meta:
        verbose_name_plural = "Rubrics"
        verbose_name = "Rubric"
        ordering = ["name"]


