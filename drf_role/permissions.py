from django.urls import resolve
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission

from drf_role.enums import RoleEnum, PermissionEnum
from drf_role.models import AccessControl


class IsAdminOrNoAccess(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        try:
            return request.user.profile.role.type == RoleEnum.Admin.value
        except AttributeError:
            return False


class BaseRolePermission(BasePermission):
    SAFE_MODELS = list()

    @staticmethod
    def permission_analyzer(request=None, view=None):
        """
        This will help to analyze the permissions and model object level permission
        :param request: django default request
        :param view: ViewClass of each view in MVC it's (C)Controller
        :return:
        """
        try:
            user = request.user
            user_role = user.profile.role
            url_name = resolve(request.path_info).url_name
            access = AccessControl.objects.filter(role_id=user_role.pk, url_name=url_name).first()
            if access:
                permission_types = access.permissions.values_list('access_type', flat=True)
                write_permission = PermissionEnum.WRITE.value
                no_access = PermissionEnum.NO_ACCESS.value

                if no_access in permission_types:
                    return False

                if write_permission in permission_types:
                    return True
                else:
                    return request.method in SAFE_METHODS
            else:
                return True
        except AttributeError:
            return False

    def has_permission(self, request, view):
        return self.permission_analyzer(request=request)

    def has_object_permission(self, request, view, obj):
        return self.permission_analyzer(request=request)
