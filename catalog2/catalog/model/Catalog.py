from django.db import models


class Catalog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=True, blank=True)


