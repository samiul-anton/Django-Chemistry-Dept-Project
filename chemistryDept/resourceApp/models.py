from django.db import models

# Create your models here.

class labFacility(models.Model) :
    image_heading = models.TextField(max_length=100)
    image_caption = models.TextField(max_length=200)
    lab_image = models.ImageField(null=True, blank=True, upload_to="Images/")
    def __str__(self):
        return self.image_heading
