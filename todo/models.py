from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=20)
    details = models.TextField()
    date = models.DateField(default=timezone.now)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
