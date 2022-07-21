from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.



"""def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%m%d%Y')
    filename = "%s%s", (timeNow, old_filename)
    return os.path.join(filenam)"""
class Userinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_image = models.ImageField(null=True, blank=True, upload_to="Images/")

    def __str__(self):
        return self.user.username
