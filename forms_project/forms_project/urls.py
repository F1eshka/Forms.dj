from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.user_login),
    path('calc/', views.calc),
    path('register/', views.register),
    path('programmer/', views.programmer_day),
]