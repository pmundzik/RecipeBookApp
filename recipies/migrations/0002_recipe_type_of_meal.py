# Generated by Django 3.0.6 on 2020-05-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='type_of_meal',
            field=models.CharField(default='dinner', max_length=255),
        ),
    ]
