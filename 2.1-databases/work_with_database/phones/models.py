from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])
    slug = models.SlugField(blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
