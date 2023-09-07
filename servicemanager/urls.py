# servicemanager/urls.py

from django.urls import path
from servicemanager import views

urlpatterns = [
    path("", views.home, name='home'),
    path("user/", views.user, name='user'),
    path("manage/", views.accountmanager, name='accountmanager'),
    path('user/<str:userId>', views.display_user, name = 'display_user'),
]
