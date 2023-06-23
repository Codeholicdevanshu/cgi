
from django.urls import path
from .views import *
from  app import views
urlpatterns = [
    path('',views.Register,name='register'),
    path('login',views.loginUser,name='login'),
    path('logout',views.Logout,name='logout'),
    path('base',views.base,name='base')

]