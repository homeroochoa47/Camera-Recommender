from django.db import models

# Create your models here.
class Camera(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return (self.name)
    
    def name_for_url(self):
        new_name = self.name.replace(' ', '+')
        print (new_name)
        return new_name