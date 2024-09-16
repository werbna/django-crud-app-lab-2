from django.shortcuts import render, redirect # type: ignore
from django.views.generic.edit import CreateView, UpdateView, DeleteView # type: ignore
from .models import Recipe, Comment # type: ignore
from .forms import CommentForm # type: ignore
from django.contrib.auth.views import LoginView # type: ignore

# Create your views here.
class home(LoginView):
    template_name = 'home.html'

def about(req):
    return render(req, 'about.html')

def recipes_index(req):
    recipes = Recipe.objects.all()
    return render(req, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(req, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    comment_form = CommentForm()
    return render(req, 'recipes/detail.html', {
    'recipe': recipe, 
    'comment_form': comment_form
    })

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = '/recipes/'
    
    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['description', 'ingredients', 'prep_time', 'cook_time', 'instructions', 'servings', 'imageurl']
    
class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'
    
def add_comment(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = CommentForm(request.POST)
    
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.recipe = recipe
        new_comment.user = request.user
        new_comment.save() 
    return redirect('recipe_detail', recipe_id=recipe_id)