from django.db import models
    
class Tag(models.Model):
    name = models.URLField(max_length=30)
    
class City(models.Model):
    name = models.URLField(max_length=30)

class CommonImage(models.Model):
    url = models.URLField(max_length=30)
    city = models.ForeignKey(City)
    class Meta:
        abstract = True
    
class CityImage(models.Model):
    description = models.TextField()
    
    
class SceneImage(CityImage):
    name = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tag)
    date = models.DateField()