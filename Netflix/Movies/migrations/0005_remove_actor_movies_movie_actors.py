# Generated by Django 5.0.4 on 2024-04-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0004_actor_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movies',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='Movies.actor'),
        ),
    ]