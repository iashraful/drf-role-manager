from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey('drf_role.Role', on_delete=models.SET_NULL, null=True, related_name='user_profiles')
