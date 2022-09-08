from django.db import models

# Create your models here.
class new(models.Model) :
    news_title = models.TextField(max_length=100)
    news_cover = models.ImageField(null=True, blank=True, upload_to="Images/")
    news_description = models.TextField(max_length=100)
    news_category = models.TextField(max_length=100)
    news_url = models.TextField(max_length=100)
    featured = models.BooleanField()

    def __str__(self):
        return self.news_title
    def news_info(self):
        news_info = [self.news_title , str(self.news_cover), self.news_description, self.news_category , self.news_url,self.featured]
        return news_info
