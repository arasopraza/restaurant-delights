from django.shortcuts import redirect

from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
  template_name = "restaurant/home.html"

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

class IngredientsView(LoginRequiredMixin, ListView):
  template_name="restaurant/ingredients.html"
  model = Ingredient

class AddIngredientsView(LoginRequiredMixin, CreateView):
  template_name="restaurant/add_ingredients.html"
  model = Ingredient
  form_class = IngredientForm

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    template_name = "restaurant/update_ingredient.html"
    model = Ingredient
    form_class = IngredientForm

class MenuView(LoginRequiredMixin, ListView):
  template_name="restaurant/menu.html"
  model = MenuItem

class AddMenuItemView(LoginRequiredMixin, CreateView):
  template_name="restaurant/add_menu_item.html"
  model = MenuItem
  form_class = MenuItemForm

class AddRecipeRequirementView(LoginRequiredMixin, CreateView):
  template_name="restaurant/add_recipe_requirement.html"
  model = RecipeRequirement
  form_class = RecipeRequirementForm

class PurchasesView(LoginRequiredMixin, ListView):
  template_name="restaurant/purchases.html"
  model = Purchase

class AddPurchaseView(LoginRequiredMixin, TemplateView):
  template_name="restaurant/add_purchase.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
    return context
  
  def post(self, request):
    menu_item_id = request.POST["menu_item"]
    menu_item = MenuItem.objects.get(pk=menu_item_id)
    requirements = menu_item.reciperequirement_set
    purchase = Purchase(menu_item=menu_item)

    for requirement in requirements.all():
      required_ingredient = requirement.ingredient
      required_ingredient.quantity -= requirement.quantity
      required_ingredient.save()
    
    purchase.save()
    return redirect("/purchases")

class ReportView(LoginRequiredMixin, TemplateView):
  template_name = "restaurant/reports.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["purchases"] = Purchase.objects.all()
    revenue = Purchase.objects.aggregate(
      revenue=Sum('menu_item__price'))["revenue"]
    total_cost = 0

    for purchase in Purchase.objects.all():
      for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
        total_cost += recipe_requirement.ingredient.unit_price * recipe_requirement.quantity
    
    context["revenue"] = revenue
    context["total_cost"] = total_cost
    context["profit"] = revenue - total_cost

    return context

def log_out(request):
    logout(request)
    return redirect("/")