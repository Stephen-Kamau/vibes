from django.db import models
from signup.models import signup
# Create your models here.

class Followers(models.Model):
    fid = models.AutoField(primary_key = True)
    is_following = models.BooleanField(default = False)
    follower = models.ForeignKey(signup , related_name = "followers" ,  on_delete = models.CASCADE)
    following = models.ForeignKey(signup , related_name = "following" , on_delete = models.CASCADE)

    class Meta:
        db_table = "Followers"
