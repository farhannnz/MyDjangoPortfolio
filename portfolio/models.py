
# Create your models here.
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    # Value from 0 to 1

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    marks = models.FloatField()
    certificate = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.institution

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField()
    visit_link = models.URLField()

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
