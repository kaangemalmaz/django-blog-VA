from django.urls import reverse
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,upload_to='images')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})
