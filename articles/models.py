from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail',kwargs={'pk':self.pk})    


class Comment(models.Model):
    article=models.ForeignKey(Article ,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    author= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment


    def get_absolute_url(self):   
        return reverse('article_list') 