from django.urls import path
import records.views as views


urlpatterns = [
    path('', views.GetRecordsView.as_view(), name='get-records'),
]