from django.db import models

# Create your models here.
class courseAnnouncemets(models.Model):
    course_name = models.TextField(max_length=200)
    instructor_name = models.TextField(max_length=200)
    course_description = models.TextField()
    number_of_credit = models.IntegerField()
    course_content = models.TextField()
    course_cover = models.ImageField(null=True, blank=True, upload_to="Images/")

    def __str__(self):
        return self.course_name
    def getCourseData(self):
        data = [self.course_name , self.instructor_name,self.course_description ,self.number_of_credit,str(self.course_cover),self.course_content]
        return data

class seminer(models.Model):
    seminer_title = models.CharField(max_length=200)
    seminer_description = models.TextField(max_length=500)
    seminer_details = models.TextField(max_length=500)
    seminer_speakers = models.CharField(max_length=500)
    seminer_datetime = models.DateTimeField ( blank = False)
    seminer_location = models.CharField(max_length=200)
    seminer_notes = models.TextField(max_length=500)
    seminar_cover = models.ImageField(null=True, blank=True, upload_to="Images/")
    featured = models.BooleanField()

    def __str__(self):
        return self.seminer_title
    def getSeminerData(self):
        data = [self.seminer_title , self.seminer_description,self.seminer_details ,self.seminer_speakers,str(self.seminer_datetime),self.seminer_location, str(self.seminar_cover),self.featured,self.seminer_notes]
        return data
