from django.contrib.auth.models import User
from django.db import models
from shortening.settings import SHORT_URL_LENGTH_BOUNDS

maximum_l = SHORT_URL_LENGTH_BOUNDS[1]


class URLs(models.Model):
    shortURL = models.CharField(max_length=maximum_l, primary_key=True)
    targetURL = models.CharField(max_length=2083)
    countV = models.IntegerField(default=0)
    SubUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
