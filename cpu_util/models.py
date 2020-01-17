from django.db import models
from django.utils import timezone


class Record(models.Model):
    record_datetime = models.DateTimeField(default=timezone.now(), null=False)
    record_cpu_data = models.DecimalField(max_digits=4, decimal_places=1, blank=False)
