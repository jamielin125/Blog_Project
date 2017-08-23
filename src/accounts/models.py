from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def upload_location(instance,  filename):

    return "Avatar-%s/%s" %(instance.user.username, filename)


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	avatar = models.ImageField(
	    	upload_to=upload_location, 
	            default='default-user-image.png',
	            null=True, 
	            blank=True, 
	            width_field="width_field", 
	            height_field="height_field")
	height_field = models.IntegerField(default=50)
	width_field = models.IntegerField(default=50)

	def __unicode__(self):
		return str(self.user.username)

	def __str__(self):
		return str(self.user.username)
		

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
