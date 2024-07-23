from django.shortcuts import redirect

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .models import Ingredient, MenuItem, Purchase
from .forms import IngredientForm

# Create your views here.
class HomeView(TemplateView):
  template_name = "restaurant/home.html"

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

class IngredientsView(ListView):
  template_name="restaurant/ingredients.html"
  model = Ingredient

class AddIngredientsView(CreateView):
  template_name="restaurant/add_ingredients.html"
  model = Ingredient
  form_class = IngredientForm

class MenuView(ListView):
  template_name="restaurant/menu.html"
  model = MenuItem

class PurchasesView(ListView):
  template_name="restaurant/purchases.html"
  model = Purchase