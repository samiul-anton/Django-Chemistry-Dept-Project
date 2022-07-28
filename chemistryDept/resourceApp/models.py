from django.db import models

# Create your models here.

class labFacility(models.Model) :
    image_heading = models.TextField(max_length=100)
    image_caption = models.TextField(max_length=200)
    lab_image = models.ImageField(null=True, blank=True, upload_to="Images/")
    def __str__(self):
        return self.image_heading

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
