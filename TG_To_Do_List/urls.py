from django.contrib import admin
from . import views
from django.urls import path, include
from register import views as r_view

urlpatterns = [

    path('register/', r_view.register, name="register"),
    path('connected/', views.main, name="main"),
    path('connected/add_item/', views.add_item),
    path('connected/delete_item/<int:id_to_delete>/', views.delete_item),
    path('', include("django.contrib.auth.urls")),
    path('', views.login, name="login")

]
