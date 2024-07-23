from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
  path('ingredients/add', views.AddIngredientsView.as_view(), name="add_ingredient"),
  path('menu/', views.MenuView.as_view(), name="menu"),
  path('menu/add', views.AddMenuItemView.as_view(), name="add_menu_item"),
  path('reciperequirement/new', views.AddRecipeRequirementView.as_view(), name="add_recipe_requirement"),
  path('purchases', views.PurchasesView.as_view(), name="purchases"),
]
