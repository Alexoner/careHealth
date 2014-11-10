from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # This line in required.Links UserProfile to a User model instance
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__method to return out something meaningful
    def __unicode__(self):
        return self.username
