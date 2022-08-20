from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at =models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug = self.name
        self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

class Post(models.Model):
    STATUS_TYPE = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish')
    )
    title = models.CharField(max_length=1000)
    content = models.TextField()
    image = models.ImageField(upload_to="simage/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_TYPE)
    approval = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = self.title
        self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000)
    name = models.CharField(max_length=50)
    created_at =models.DateTimeField(auto_now_add=True)
# Create your models here.
