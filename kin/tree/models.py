import datetime as dt

from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import ValidationError
from django.db import models


def max_year_validator(value):
    """Raises a ValidationError if year is greater than the current year."""
    if value > dt.datetime.utcnow().year:
        raise ValidationError(
            '{} exceeds the current year'
        )


class Kin(models.Model):
    """Model to represent a single family member."""
    parents = models.ManyToManyField(
        'self',
        blank=True,
        related_name='children',
        related_query_name='child',
        symmetrical=False
    )
    name = models.CharField(
        max_length=200
    )
    yob = models.SmallIntegerField(
        'year of birth',
        validators=[max_year_validator],
        null=True
    )
    mob = models.PositiveSmallIntegerField(
        'month of birth',
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        blank=True,
        null=True
    )
    dob = models.PositiveSmallIntegerField(
        'day of birth',
        validators=[MinValueValidator(1), MaxValueValidator(31)],
        blank=True,
        null=True
    )
    deceased = models.BooleanField(
        default=False
    )
    yod = models.SmallIntegerField(
        'year of death',
        validators=[MaxValueValidator(dt.datetime.utcnow().year)],
        blank=True,
        null=True
    )
    mod = models.PositiveSmallIntegerField(
        'month of death',
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        blank=True,
        null=True
    )
    dod = models.PositiveSmallIntegerField(
        'day of death',
        validators=[MinValueValidator(1), MaxValueValidator(31)],
        blank=True,
        null=True
    )

    class Meta:
        default_related_name = 'kin'
        get_latest_by = ['yob', 'mob', 'dob']
        ordering = ['-yob', '-mob', '-dob']
        verbose_name_plural = 'kin'

    @property
    def age(self):
        if not self.deceased:
            now = dt.datetime.utcnow()
            if self.mob and (self.mob < now.month
                             or (self.dob and self.dob < now.day)):
                year = now.year - 1
            else:
                year = now.year
            return year - self.yob
        else:
            return None
