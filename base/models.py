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
    # track=models.TextField(default="Networking")
    bio=models.TextField(blank=True)
    avatar = ResizedImageField(size=[300, 300], default='https://cdn-icons-png.flaticon.com/512/6596/6596121.png')
    # event_participant = models.BooleanField(default=True, null=True)

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username']

    class Meta:
        ordering = ['avatar']

class Resource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True,editable=False)
    name= models.CharField(max_length=200,  null=True)
    preview_text = models.TextField(null=True, blank=True)
    document=models.FileField(upload_to='uploads/', max_length=100)
    description=models.TextField(blank=True)
    available=models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Track(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True,editable=False)
    name= models.CharField(max_length=200,  null=True)
    participants = models.ManyToManyField(User,through='TrackParticipant', blank=True, related_name='tracks',editable=True)
    def __str__(self):
        return str(self.name)

class TrackParticipant(models.Model):
    participant=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    track=models.ForeignKey(Track,on_delete=models.CASCADE,blank=True)
    participating=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return  str(self.track)
    
    
