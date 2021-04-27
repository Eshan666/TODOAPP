from django.db import models

# Create your models here.

class Task(models.Model):
    user = models.CharField(max_length=100,null=True)
    note = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user