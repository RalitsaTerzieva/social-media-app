from users import views
from django.urls import path

urlpatterns = [
    path("login/",views.user_login,name='login'),
]