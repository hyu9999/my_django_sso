from rest_framework import mixins, viewsets

from sso.apps.users.models import UserProfile
from sso.apps.users.serializers import UserProfileSerializer


class UserProfileViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.owned_by(self.request.user)
