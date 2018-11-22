from rest_framework.serializers import ModelSerializer

from role_test_app.models import UserProfile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
