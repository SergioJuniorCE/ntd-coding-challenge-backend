from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Own
    path('users/', include('users.urls')),
    path('operations/', include('operations.urls')),
    path('records/', include('records.urls')),
    # Admin
    path('admin/', admin.site.urls),
    # DJR
    path('api-auth/', include('rest_framework.urls'))
]
