from django.contrib import admin
from . import views
from django.urls import path, include
from register import views as r_view

urlpatterns = [

    # path('login/', views.login),
    path('register/', r_view.register, name="register"),
    path('admin/', admin.site.urls),
    path('add_item/', views.add_item),
    path('delete_item/<int:id_to_delete>/', views.delete_item),
    path('', r_view.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    # path('', views.login),
    # path('', include("django.contrib.auth.urls")),
]
