from django.db import models

# Create your models here.
class signup(models.Model):
    email = models.EmailField(primary_key=True , max_length = 60)
    username = models.CharField(max_length = 30)
    pnumber = models.IntegerField(max_length = 30)
    location = models.CharField(max_length = 30)
    hobby = models.CharField(max_length = 30)
    profilepic = models.FileField()
    password = models.CharField(max_length = 60)

    class Meta:
        db_table = "signup"
