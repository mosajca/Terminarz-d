from django.contrib.auth import get_user_model
from django.db import models


class Event(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
