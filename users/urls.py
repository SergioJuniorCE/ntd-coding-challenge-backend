from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('register', views.UserRegister.as_view(), name='register'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('user', views.UserView.as_view(), name='user'),
    path('reset-balance', views.ResetBalanceView.as_view(), name='reset-balance'),
    path('get-balance', views.GetBalanceView.as_view(), name='get-balance'),
]
