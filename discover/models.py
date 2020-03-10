from django.db import models
from signup.models import signup
# Create your models here.

class Followers(models.Model):
    fid = models.AutoField(primary_key = True)
<<<<<<< HEAD
    follower = models.ForeignKey(signup , related_name = "followers" ,  on_delete = models.CASCADE)
    # test = models.CharField(max_length = 34)
=======
    is_following = models.BooleanField(default = False)
    follower = models.ForeignKey(signup , related_name = "followers" ,  on_delete = models.CASCADE)
>>>>>>> upstream/master
    following = models.ForeignKey(signup , related_name = "following" , on_delete = models.CASCADE)
    is_following = models.BooleanField(default = False)

    class Meta:
        db_table = "Followers"
