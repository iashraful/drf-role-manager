from rest_framework.generics import ListCreateAPIView

from drf_role.permissions import BaseRolePermission
from role_test_app.models import UserProfile
from role_test_app.serializers import ProfileSerializer


class ProfileListView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (BaseRolePermission,)
