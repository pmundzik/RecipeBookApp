from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    prepare_time = models.IntegerField()
    portion = models.IntegerField()
    image_url = models.CharField(max_length=2083)
