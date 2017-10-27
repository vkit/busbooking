from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


From = (
    ('1', 'Hubli'),
    ('2', 'Bangalore'),
    ('3', 'Mumbai')
)

To = (
    ('1', 'Hubli'),
    ('2', 'Bangalore'),
    ('3', 'Mumbai')
)


class CityDetails(models.Model):
    fromcity = models.CharField(
        max_length=40,
        choices=From, default='empty')
    to = models.CharField(
        max_length=40,
        choices=To, default='empty')
    created_by = models.ForeignKey(User, blank=True, null=True)
    date_of_journey = models.DateTimeField(default=timezone.now)
    return_journey = models.DateTimeField(default=timezone.now)
