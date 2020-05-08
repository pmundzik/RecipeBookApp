from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe


def index(request):
    # recipes = Recipe.objects.all()
    return render(request, 'index.html')


def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'all_recipes.html', {'recipes': recipes})


def all_breakfasts(request):
    breakfasts = Recipe.objects.all()
    return render(request, 'all_breakfasts.html', {'recipes': breakfasts})


def all_lunches(request):
    lunches = Recipe.objects.all()
    return render(request, 'all_lunches.html', {'recipes': lunches})


def all_salads(request):
    salads = Recipe.objects.all()
    return render(request, 'all_salads.html', {'recipes': salads})


def all_dinners(request):
    dinners = Recipe.objects.all()
    return render(request, 'all_dinners.html', {'recipes': dinners})


def all_soups(request):
    soups = Recipe.objects.all()
    return render(request, 'all_soups.html', {'recipes': soups})


def all_desserts(request):
    desserts = Recipe.objects.all()
    return render(request, 'all_desserts.html', {'recipes': desserts})



def new_recipe(request):
    return HttpResponse('New Recipe')
