from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    mobile=models.CharField(max_length=10,null=True)


    def __str__(self):
        return self.username

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.TextField(max_length=540,null=True,blank=True)

    def __str__(self):
        return self.text


class Following(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    following=models.ManyToManyField(User,related_name='follow_to')

    def __str__(self):
        return self.user
