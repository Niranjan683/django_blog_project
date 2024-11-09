from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url= models.URLField(null=True) # default length is 200. null argument is used to nullable whch means some post doesn't contain images
    created_at = models.DateTimeField(auto_now_add=True)

 

    def __str__(self) :
        return self.title