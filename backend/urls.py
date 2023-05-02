from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Own
    path('v1/users/', include('users.urls')),
    path('v1/operations/', include('operations.urls')),
    path('v1/records/', include('records.urls')),
    # Admin
    path('admin/', admin.site.urls),
    # DJR
    path('api-auth/', include('rest_framework.urls'))
]
