from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    image=RichTextUploadingField(null=True, blank=True)
    content=RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.title
class Comment(models.Model):
    title= models.CharField(max_length=100)
    comment=models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.title


class Package(models.Model):
    title= models.CharField(max_length=100)
    content=RichTextUploadingField()
    detail=RichTextUploadingField()
    price= models.TextField()
    teacher= models.TextField()
    time= models.TextField()
    file= models.FileField(upload_to='fileZip/',null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)



    def __str__(self):
        return self.title

class OnlineLearn(models.Model):
    title= models.CharField(max_length=100)
    content=RichTextUploadingField()
    detail=RichTextUploadingField()
    price= models.TextField()
    teacher= models.TextField()
    time= models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)



    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField()
    phone =models.IntegerField()
    description =RichTextUploadingField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Sell(models.Model):
    username = models.CharField(max_length=100)
    nameOfmyClass =models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add= True,auto_now=False,auto_created=True)


class SellOnline(models.Model):
    username = models.CharField(max_length=100)
    nameOfmyClass =models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add= True,auto_now=False,auto_created=True)
