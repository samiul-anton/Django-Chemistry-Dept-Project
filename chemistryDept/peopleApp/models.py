from django.db import models

class faculty(models.Model) :
    name = models.TextField(max_length=100)
    faculty_image = models.ImageField(null=True, blank=True, upload_to="Images/")
    email = models.EmailField(max_length=50)
    designation = models.TextField(max_length=100)
    experience = models.TextField(max_length=100)
    about = models.TextField(max_length=500, null=True)
    url = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    def faculty_info(self):
        faculty_info = [self.name , str(self.faculty_image), self.email, self.designation , self.experience , self.about , self.url]
        return faculty_info
class staff(models.Model):
    name = models.TextField(max_length=100)
    staff_image = models.ImageField(null=True, blank=True, upload_to="Images/")
    email = models.EmailField(max_length=50)
    designation = models.TextField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
    def staff_info(self):
        staff_info = [self.name , str(self.staff_image), self.email, self.designation , self.description]
        return staff_info
class student(models.Model):
    student_type = (
         ("Graduate","Graduate"),
         ("Undergrad","Undergrad"),
        )
    name = models.TextField(max_length=100)
    student_image = models.ImageField(null=True, blank=True, upload_to="Images/")
    email = models.EmailField(max_length=50)
    student_type = models.TextField(choices=student_type)

    def __str__(self):
        return self.name
    def student_info(self):
        student_info = [self.name , str(self.student_image), self.email, self.student_type]
        return student_info
