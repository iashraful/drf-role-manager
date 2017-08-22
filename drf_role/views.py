from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_role.helpers.url_list_helper import get_urls
from drf_role.models import Role, Permission, AccessControl
from drf_role.permissions import IsAdminOrDeveloperOrNoAccess
from drf_role.serializers import RoleSerializer, PermissionSerializer, AccessControlSerializer, AllViewListSerializer


class RoleView(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrDeveloperOrNoAccess,)
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class PermissionView(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrDeveloperOrNoAccess,)
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    models = (Permission,)


class AccessControlView(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrDeveloperOrNoAccess,)
    serializer_class = AccessControlSerializer
    queryset = AccessControl.objects.all()

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            permissions = request.data.get('permissions')
            permission_instance_list = [p for p in Permission.objects.filter(pk__in=permissions)]
            serializer = AccessControlSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                if instance:
                    instance.permissions.add(*permission_instance_list)
                    return Response(serializer.data)
            return Response(serializer.data)


class AllUrlList(APIView):
    permission_classes = (IsAdminOrDeveloperOrNoAccess,)

    def get(self, request, *args, **kwargs):
        data = {
            'url_names': get_urls()  # it will be a list
        }
        serializer = AllViewListSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data)
        return serializer.data
