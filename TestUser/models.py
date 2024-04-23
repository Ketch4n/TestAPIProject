from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Birthday = models.DateField()
