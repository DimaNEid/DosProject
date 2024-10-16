from django.db import models
from catalog.model.Catalog import Catalog


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    cost = models.IntegerField(max_length=120, null=True, blank=True)
    topic = models.CharField(max_length=120, null=True, blank=True)
    count = models.IntegerField(max_length=120, null=True, blank=True)
    catalog_id = models.ForeignKey(Catalog, on_delete=models.CASCADE)
