from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # This line in required.Links UserProfile to a User model instance
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    phone_number = models.CharField(max_length=16, blank=True)
    identification_number = models.CharField(max_length=18, blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # Override the __unicode__method to return out something meaningful
    def __unicode__(self):
        return self.username
