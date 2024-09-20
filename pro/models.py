from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #attributes of the user
    username = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(unique=True,max_length=10)
    def __str__(self):
        return self.user.username







class blogs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=15)
    text = models.TextField(max_length=4000,null=True)
    date = models.DateTimeField(default=now())
    uname = models.CharField(max_length=30,default='unknown')
    love = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)



class drafts(models.Model):
    models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=15)
    text = models.TextField(max_length=4000,null=True)
    date = models.DateTimeField(default=now())
    uname = models.CharField(max_length=30,default='unknown')











