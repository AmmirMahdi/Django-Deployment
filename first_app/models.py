from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):

    top_name = models.CharField(max_length=220, unique=True)


    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    top = models.ForeignKey(Topic, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    name = models.CharField(max_length=220,unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserProfileInfos(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)

    potfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)


    def __str__(self):
        return self.user.userame
