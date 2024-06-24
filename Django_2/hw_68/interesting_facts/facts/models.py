from django.db import models


class Facts(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='facts/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
