# Generated by Django 5.0.4 on 2024-05-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_remove_actor_movies_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='Movies.actor'),
        ),
    ]
