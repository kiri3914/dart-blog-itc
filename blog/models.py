from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug":self.slug})



class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True,  null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug":self.slug})



def upload_post(instance, filename):
    return f'photo/{date.today()}/ {filename}'

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True,  null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name='post_user')
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=upload_post, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)

    
    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.lower()
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('post', kwargs={"slug":self.slug})

    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

