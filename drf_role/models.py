from django.db import models

from drf_role.enums import PermissionEnum, RoleEnum


class Role(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    type = models.IntegerField(unique=True)
    description = models.TextField(verbose_name='Role\'s Description', blank=True)

    def __str__(self):
        return RoleEnum(self.type).name


class Permission(models.Model):
    access_type = models.IntegerField(default=PermissionEnum.READ.value, unique=True)
    access_type_name = models.CharField(max_length=20, default=PermissionEnum.READ.name)

    def __str__(self):
        # Retrieve the enum variable. Ex: CREATE, VIEW, ...
        return PermissionEnum(self.access_type).name


class AccessControl(models.Model):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    url_name = models.CharField(max_length=30, null=True, blank=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.role.name
