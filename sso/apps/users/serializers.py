from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sso.apps.users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserProfile
        fields = '__all__'
