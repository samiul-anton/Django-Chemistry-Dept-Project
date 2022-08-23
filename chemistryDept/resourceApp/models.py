from django.db import models

# Create your models here.

class labFacility(models.Model) :
    sections = (
     ("Classrooms","Classrooms"),
     ("Labs Equipment","Labs Equipment"),
     ("Instruments","Instruments"),
    )
    lab_sections = models.TextField(choices=sections)
    image_heading = models.TextField(max_length=100)
    image_caption = models.TextField(max_length=200)
    lab_image = models.ImageField(null=True, blank=True, upload_to="Images/")
    def __str__(self):
        return self.image_heading
    def all_labfacilites_data(self):
        data = [self.image_heading , self.image_caption , str(self.lab_image),self.lab_sections]
        return data

class computing(models.Model):
    type = (
     ("Image","Image"),
     ("Video","Video"),
    )
    computing_heading = models.TextField(max_length=100)
    computing_url = models.TextField(max_length=100,null=True ,blank=True)
    computing_type = models.TextField(choices=type)
    computing_image = models.ImageField(null=True, blank=True, upload_to="Images/")

    def __str__(self):
        return self.computing_heading

    def all_computing_data(self):
        data = [self.computing_heading , self.computing_url , self.computing_type , str(self.computing_image)]
        return data


class studentService(models.Model):
    service_name = models.TextField(max_length=100)
    service_description = models.TextField(max_length=100,null=True ,blank=True)
    service_link = models.TextField(max_length=100)
    service_cover = models.ImageField(null=True, blank=True, upload_to="Images/")

    def __str__(self):
        return self.service_name

    def all_computing_data(self):
        data = [self.service_name , self.service_description , self.service_link , str(self.service_cover)]
        return data
