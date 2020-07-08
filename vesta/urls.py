from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from core.api.schemas.schema_view import schema_view
from user.api import UserModelViewSet

router = DefaultRouter()
router.register(r'user', UserModelViewSet, basename='user')

urlpatterns = [
    # API documentation and playground
    re_path(r'^api-doc/$', schema_view.with_ui('redoc', cache_timeout=0), name='api-doc'),
    re_path(r'^api-playground(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='api-playground-json'),
    re_path(r'^api-playground/$', schema_view.with_ui('swagger', cache_timeout=0), name='api-playground-ui'),

    # Admin
    re_path(r'admin/', admin.site.urls),

    # Authentication token
    re_path(r'auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # API
    re_path(r'', include(router.urls))
]

urlpatterns += staticfiles_urlpatterns()
