from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    # post categories
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ["name"]


    def __str__(self):
        return f'{self.name}'


class Topic(models.Model):
    # post topics
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    # tags to associate with posts
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.title}'
        # text = self.text
        # text = f'{" ".join(text.split()[:5])}'
        # if len(text) > 5:
        #     text = text + ' ...'
        # return text


class Page(models.Model):
    # static pages
    title = models.CharField(max_length=60)
    text = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.title}'
        # text = self.text
        # text = f'{" ".join(text.split()[:5])}'
        # if len(text) > 5:
        #     text = text + ' ...'
        # return text