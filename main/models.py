from django.contrib.auth import get_user_model
from django.db import models


class Event(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='nazwa')
    description = models.CharField(max_length=255, verbose_name='opis')
    start_date_time = models.DateTimeField(verbose_name='początek')
    end_date_time = models.DateTimeField(verbose_name='koniec')

    class Meta:
        ordering = ['start_date_time']
