from users import views
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.user_login,name='login'),
    path("logout/",auth_view.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
]