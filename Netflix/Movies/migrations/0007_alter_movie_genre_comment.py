# Generated by Django 5.0.4 on 2024-05-05 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0006_alter_actor_gender_alter_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Children', 'Children'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], max_length=50),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.movie')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.actor')),
            ],
            options={
                'db_table': 'Comments',
                'ordering': ['created_date'],
            },
        ),
    ]