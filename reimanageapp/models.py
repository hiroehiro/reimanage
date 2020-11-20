from django.db import models

# Create your models here.

class MemoModel(models.Model):
    goods = models.CharField(max_length=100)
    goods_number = models.IntegerField(null=True)
    bought = models.BooleanField(null=True)
    