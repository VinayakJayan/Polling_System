from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Construct the full path to the default image
        img_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        try:
            img = Image.open(img_path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(img_path)
        except FileNotFoundError:
            # Handle the missing default image gracefully
            print(f"Default image not found: {img_path}")

class UpdateProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)

    def _str_(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
