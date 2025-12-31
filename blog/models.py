from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length= 200)
    image = models.CharField(max_length= 2025)
    content = RichTextField()
    describe = models.CharField(max_length= 300)
    date = models.DateTimeField (auto_now_add= True)
    likes = models.PositiveIntegerField(default= 0)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    posts = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length= 300)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)