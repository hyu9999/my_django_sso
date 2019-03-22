from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True
    )
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Profile for {}'.format(self.user.username)
