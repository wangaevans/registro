from django.db import models
from datetime import datetime
import time
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
import uuid

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=100,null=True)
    huawei_id=models.CharField(unique=True,max_length=100)
    phone=models.CharField(unique=True,max_length=100)
    bio=models.TextField(blank=True)
    avatar = ResizedImageField(upload_to='profile_pictures',size=[300, 300], default='static/images/profile_pictures/pexels-guilherme-rossi-1755683.png')
    
    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username']
    

    class Meta:
        ordering = ['avatar']

class HuaweiTrack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    participants = models.ManyToManyField(User, through='Participant')
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    banner = models.URLField(max_length=500)

    def __str__(self):
        return self.name

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(HuaweiTrack, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
    
class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True,editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner = models.URLField(max_length=200)
    url = models.URLField()
    track = models.ForeignKey(HuaweiTrack, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
