from django.urls import path
from . import views  # from the current folder I import view folder

urlpatterns = [
    path('', views.index),
    path('new', views.new_recipe)
]