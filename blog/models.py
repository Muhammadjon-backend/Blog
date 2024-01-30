from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="articles/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


