from django.urls import path

from operations import views

urlpatterns = [
    path('random_generate', views.random_generate, name='random-generate'),
    path('calculate', views.Calculate.as_view(), name='calculate'),
    path('get_random_string', views.GetRandomString.as_view(), name='get-random-string'),
]
