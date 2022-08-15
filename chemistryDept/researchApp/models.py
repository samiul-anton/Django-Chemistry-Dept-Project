from django.db import models
from peopleApp.models import faculty

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
    def research_area_info(self):
        data_info = [self.research_fields , str(self.research_cover), self.research_title, self.research_description , self.project_include , self.publication_video , self.publication_details]
        return

class research_overview(models.Model):
    overview_facutly = models.ForeignKey(faculty, on_delete=models.CASCADE)
    Sustainability = models.TextField(max_length=250,null=True)
    Energy = models.TextField(max_length=250,null=True)
    Artificial_Intelligence = models.TextField(max_length=250,null=True)
    Biomedical = models.TextField(max_length=250,null=True)
    Education = models.TextField(max_length=250,null=True)


    def __str__(self):
        return self.overview_facutly.name
    def research_overview_info(self):
        data_info = [self.overview_facutly.id , self.Sustainability ,self.Energy,self.Artificial_Intelligence,self.Education ]
        return data_info

class research_by_direction(models.Model):
    research_fields_choice = (
     ("Sustainability Energy","Sustainability Energy"),
     ("Medical","Medical"),
    )
    research_fields = models.TextField(choices=research_fields_choice);
    project_name = models.CharField(max_length=250)
    project_category = models.CharField(max_length=250)
    project_date = models.DateField()
    project_link = models.CharField(max_length=250)
    project_description = models.TextField(max_length=250)
    research_cover_1 = models.ImageField(null=True, blank=True, upload_to="Images/")
    research_cover_2 = models.ImageField(null=True, blank=True, upload_to="Images/")
    research_cover_3 = models.ImageField(null=True, blank=True, upload_to="Images/")

    def __str__(self):
        return self.project_name+":"+self.research_fields
    def research_direction_info(self):
        data_info = [self.research_fields , str(self.research_cover_1), str(self.research_cover_2), str(self.research_cover_3), self.project_name, self.project_category , self.project_date , self.project_link , self.project_description]
        return data_info
