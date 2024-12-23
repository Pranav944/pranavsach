

from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.title

