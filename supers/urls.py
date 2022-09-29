from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_list),
    path('<int:pk>/', views.super_detail),
]