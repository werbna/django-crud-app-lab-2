from django.shortcuts import render # type: ignore
from django.views.generic.edit import CreateView, UpdateView, DeleteView # type: ignore
from .models import Recipe, Comment # type: ignore

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
    success_url = '/recipes/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['description', 'ingredients', 'prep_time', 'cook_time', 'instructions', 'servings', 'imageurl']
    
class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'
    
class CommentCreate(CreateView):
    model = Comment
    fields = ['comment', 'text']
    success_url = '/recipes/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
      
def add_comment(req, recipe_id):
    form = CommentForm(req.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.recipe_id = recipe_id
        new_comment.save()
    success_url = '/recipes/<int:recipe_id>/'