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

class UserSharedFiles(models.Model):
    file_id = models.IntegerField()
    requested_user_id = models.IntegerField()
    shared_user_id = models.IntegerField()

    def __str__(self):
        return str(self.file_id) +' '+ str(self.requested_user_id) +' '+ str(self.shared_user_id)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)

