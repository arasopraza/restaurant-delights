from django.shortcuts import redirect

from django.views.generic import TemplateView, ListView

from .models import Ingredient, MenuItem, Purchase

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