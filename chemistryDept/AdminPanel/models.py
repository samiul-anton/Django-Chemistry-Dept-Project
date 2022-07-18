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




class research_by_area(models.Model):
    research_fields_choice = (
     ("Chemistry","Chemistry"),
     ("Chemical Engineering","Chemical Engineering"),
     ('Biomedical Engineering',"Biomedical Engineering"),
    )
    research_fields = models.TextField(choices=research_fields_choice);
    research_title = models.CharField(max_length=250)
    research_cover = models.ImageField(null=True, blank=True, upload_to="Images/")
    research_description = models.TextField(max_length=250)
    project_include = models.TextField(max_length=250)
    publication_video = models.CharField(max_length=250)
    publication_details = models.TextField(max_length=250)


    def __str__(self):
        return self.research_title+":"+self.research_fields
