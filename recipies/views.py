from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe


def index(request):
    recipies = Recipe.objects.all()
    return render(request, 'index.html', {'recipies': recipies})


def new_recipe(request):
    return HttpResponse('New Recipe')
