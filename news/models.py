from django.db import models


class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)

    def save_editor(self):
        self.save()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']


class Tags(models.Model):
    name = models.CharField(max_length=30)

    def ___str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)
# Create your models here.
