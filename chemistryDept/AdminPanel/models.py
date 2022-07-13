from django.db import models
import datetime
import os
# Create your models here.

"""def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%m%d%Y')
    filename = "%s%s", (timeNow, old_filename)
    return os.path.join(filenam)"""


class faculty(models.Model):
    name = models.TextField(max_length=100)
    faculty_image = models.ImageField(null=True, blank=True, upload_to="Images/")
    email = models.EmailField(max_length=50)
    designation = models.TextField(max_length=100)
    experience = models.TextField(max_length=100)
    about = models.TextField(max_length=500, null=True)