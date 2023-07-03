from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name="baslik")
    content = models.TextField(verbose_name="icerik")
    publishingDate = models.DateTimeField(verbose_name="yayinlanma tarihi")

    def __str__(self):
        return self.title