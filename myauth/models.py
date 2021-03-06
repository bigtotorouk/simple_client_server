from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    avatar = models.ImageField(upload_to="images/",default="images/avatar_default.jpg", blank=True, null=True)
    signature = models.CharField(blank=True, max_length=200)
    user = models.OneToOneField(User)

#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)
#post_save.connect(create_user_profile)