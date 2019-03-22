from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
# from simple_sso.sso_server.apps import SimpleSSOServer

# test_server = SimpleSSOServer()  
  
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('rest_auth.urls')),
    url(r'^api/auth/registration/', include('rest_auth.registration.urls')),
    # url('^server/', include(test_server.get_urls())),  
    url(r'^api/users/', include('sso.apps.users.urls')),
    url(r'^cas/', include('mama_cas.urls'))
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^api/docs/', get_swagger_view(title='SSO API')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = 'SSO'
admin.site.site_header = 'SSO'
