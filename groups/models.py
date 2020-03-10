from django.db import models
from signup.models import signup
# Create your models here.



class groups(models.Model):
    gid = models.AutoField(primary_key = True)
    group_name = models.CharField(max_length = 255)
    location = models.CharField(max_length = 100)
    gicon = models.ImageField()

    class Meta:
        db_table = "groups"


class members(models.Model):
    groupid = models.ManyToManyField(groups , related_name = "gbridge")
    memberuid = models.ForeignKey(signup , on_delete = models.CASCADE)

    class Meta:
        db_table = "members"
