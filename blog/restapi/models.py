from django.db import models

# Create your models here.

class Post(models.Model):
    title       = models.CharField(max_length=150)
    content     = models.TextField()
    published   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        returns title of post
        """
        return self.title

    class Meta:
        ordering = ['-published']