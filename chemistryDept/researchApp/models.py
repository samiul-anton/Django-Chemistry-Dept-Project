from django.db import models

# Create your models here.
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
