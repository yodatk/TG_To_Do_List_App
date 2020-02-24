from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path(r'add_item/', views.add_item),
]
