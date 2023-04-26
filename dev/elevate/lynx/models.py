from django.db import models

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=255)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):

        return self.title
    
    
    class Meta:

        verbose_name_plural = "Blog posts"
    





