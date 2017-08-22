from rest_framework import serializers

from drf_role.models import Role, Permission, AccessControl


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class AccessControlSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = AccessControl
        fields = '__all__'


class AllViewListSerializer(serializers.Serializer):
    url_names = serializers.ListField()

    class Meta:
        fields = 'url_names'
