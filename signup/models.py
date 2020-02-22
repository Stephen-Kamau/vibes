from django.db import models

# Create your models here.
class signup(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 60 , unique = True)
    username = models.CharField(max_length = 30 , unique = True)
    pnumber = models.IntegerField(max_length = 30)
    location = models.CharField(max_length = 30)
    hobby = models.CharField(max_length = 30)# , default = 'Nairobi/Kenya'
    profilepic = models.FileField()
    password = models.CharField(max_length = 255)

    class Meta:
        db_table = "signup"
