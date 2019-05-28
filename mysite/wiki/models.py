from django.db import models
from django.urls import reverse

# Create your models here.



class Page(models.Model):

    title = models.CharField(max_length=64, primary_key=True)
    content = models.TextField()
    counter = models.IntegerField(default=1)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki:detail', args=[self.title])


class UserFileUpload(models.Model):
    upload = models.FileField(upload_to='uploads/')

    
    def __str__(self):
        return self.upload.name
