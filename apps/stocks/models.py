from django.db import models

# Create your models here.


class Corporation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10)
    description = models.TextField()
    country = models.CharField(max_length=100)
    sector = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
