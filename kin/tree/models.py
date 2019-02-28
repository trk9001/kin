from django.db import models


class Kin(models.Model):
    parents = models.ManyToManyField(
        'self',
        blank=True,
        related_name='children',
        related_query_name='child',
        symmetrical=False,
    )
    name = models.CharField(
        max_length=200,
    )
