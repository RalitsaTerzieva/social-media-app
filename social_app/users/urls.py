from users import views
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.user_login,name='login'),
    path("logout/",auth_view.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path("password_change/",auth_view.PasswordChangeView.as_view(template_name='users/password_change_form.html'),name="password_change"),
    path("password_change/done/",auth_view.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name="password_change_done"),
]