from django.db import models

# Create your models here.


class sell_goods(models.Model):
    itemid = models.AutoField(primary_key = True)
    itemdesc = models.CharField(max_length = 255 )
    price = models.FloatField(max_length = 10)
    itemimg = models.FileField()
