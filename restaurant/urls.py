from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
  path('menu/', views.MenuView.as_view(), name="menu"),
]
