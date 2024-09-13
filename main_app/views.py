from django.shortcuts import render # type: ignore
from django.views.generic.edit import CreateView # type: ignore
from .models import Recipe # type: ignore

# Create your views here.
def home(req):
    return render(req, 'home.html')
  
def about(req):
    return render(req, 'about.html')
  
def recipes_index(req):
    recipes = Recipe.objects.all()
    return render(req, 'recipes/index.html', {'recipes': recipes})
  
def recipe_detail(req, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(req, 'recipes/detail.html', {'recipe': recipe})
  
class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
