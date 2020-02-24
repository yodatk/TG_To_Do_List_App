from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add_item/', views.add_item),
    path('delete_item/<int:id_to_delete>/', views.delete_item),
]
