from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username

class File(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200, default='')
    file = models.FileField(upload_to='user_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)

