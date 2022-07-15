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
    url = models.TextField(max_length=100)

    def __str__(self):
        return self.name
class staff(models.Model):
    name = models.TextField(max_length=100)
    staff_image = models.ImageField(null=True, blank=True, upload_to="Images/")
    email = models.EmailField(max_length=50)
    designation = models.TextField(max_length=100)

    def __str__(self):
        return self.name

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
