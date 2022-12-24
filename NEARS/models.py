from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    h_index = models.DecimalField(verbose_name="H-Index", max_digits=6, decimal_places=3)
