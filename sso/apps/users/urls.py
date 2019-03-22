from rest_framework import routers

from sso.apps.users.views import UserProfile
from sso.apps.users.views import UserProfileViewSet

router = routers.SimpleRouter()
router.register(r'userprofile', UserProfileViewSet)

urlpatterns = router.urls
