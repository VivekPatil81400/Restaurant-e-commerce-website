from email.policy import default
import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='profilepic.jpg', upload_to ='profile_pictures')
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username