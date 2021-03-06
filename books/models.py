from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    author = models.CharField(max_length=254, blank=False)
    isbn = models.CharField(max_length=254, blank=False)
    date = models.DateField()
    image = models.ImageField(upload_to = "images", default='images/default-image.jpg')
    
    def __str__(self):
        return self.name
        
