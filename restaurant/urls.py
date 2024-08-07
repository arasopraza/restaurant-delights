from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path("logout/", views.log_out, name="logout"),
  path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
  path('', views.HomeView.as_view(), name='home'),
  path('ingredients/', views.IngredientsView.as_view(), name="ingredients"),
  path('ingredients/add', views.AddIngredientsView.as_view(), name="add_ingredient"),
  path('ingredients/<slug:pk>/update', views.UpdateIngredientView.as_view(), name="update_ingredient"),
  path('menu/', views.MenuView.as_view(), name="menu"),
  path('menu/add', views.AddMenuItemView.as_view(), name="add_menu_item"),
  path('reciperequirement/new', views.AddRecipeRequirementView.as_view(), name="add_recipe_requirement"),
  path('purchases', views.PurchasesView.as_view(), name="purchases"),
  path('purchases/add', views.AddPurchaseView.as_view(), name="add_purchase"),
  path('reports', views.ReportView.as_view(), name="reports")
]
