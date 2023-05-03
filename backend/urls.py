from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # Own
    path('v1/users/', include('users.urls')),
    path('v1/operations/', include('operations.urls')),
    path('v1/records/', include('records.urls')),
    # Tokens
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Admin
    path('admin/', admin.site.urls),
    # DJR
    path('api-auth/', include('rest_framework.urls'))
]
