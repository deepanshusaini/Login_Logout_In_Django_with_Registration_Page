from django.urls import path
from app_one import views

app_name = 'app_one'

urlpatterns = [

    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),


]

