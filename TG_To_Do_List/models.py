from django.db import models
from django.contrib.auth.models import User

MAX_LENGTH = 200


# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    added_date = models.DateTimeField()
    text = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Todos'
