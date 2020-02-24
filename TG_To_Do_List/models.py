from django.db import models

MAX_LENGTH = 200


# Create your models here.

class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Todos'
