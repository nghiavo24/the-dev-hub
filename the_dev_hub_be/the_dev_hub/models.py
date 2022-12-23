from django.db import models

class Posting(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    posted = models.DateField()
    url = models.TextField()
    note = models.TextField(max_length=250, blank = True, null = True)

    def __str__(self):
        return self.title

# Create your models here.


class Application(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    applied = models.DateField()
    hiring_manager = models.CharField(max_length=50, blank= True, null = True)
    compensation = models.IntegerField(blank= True, null = True)
    work_site = models.CharField(max_length=50, default= 'N/A')
    location = models.CharField(max_length=50, default= 'N/A')