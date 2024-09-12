from django.shortcuts import render # type: ignore
import random

class Recipe:
    def __init__(self, day, name, description):
        self.day = day
        self.name = name
        self.description = description
        self.prep_time = random.randint(10, 60)
        self.cook_time = random.randint(10, 120)
        self.servings = random.randint(2, 8)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
names = ['Chicken Alfredo', 'Spaghetti and Meatballs', 'Tacos', 'Chicken Parmesan', 'Fish and Chips']
descriptions = [
    'A delicious pasta dish with chicken and alfredo sauce.',
    'A classic Italian dish with spaghetti noodles and meatballs.',
    'A Mexican dish with seasoned beef and tortillas.',
    'An Italian dish with breaded chicken and marinara sauce.',
    'A British dish with fried fish and french fries.'
]

recipes = [Recipe(day, name, description) for day, name, description in zip(days, names, descriptions)]

# Create your views here.
def home(req):
    return render(req, 'home.html')
def about(req):
    return render(req, 'about.html')
def recipes_index(req):
    return render(req, 'recipes/index.html', {'recipes': recipes})
