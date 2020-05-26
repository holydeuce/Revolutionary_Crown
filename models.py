from django.db import models

class User(models.Model):
    ch_name = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    gender =  models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
