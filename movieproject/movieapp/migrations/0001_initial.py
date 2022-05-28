# Generated by Django 3.2.7 on 2021-09-28 15:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comedy',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documentary',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drama',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fantasy',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Foreign',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horror',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mystery',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PopularMovies',
            fields=[
                ('genres', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Romance',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScienceFiction',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thriller',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TVMovie',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='War',
            fields=[
                ('genres', models.CharField(blank='True', max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Western',
            fields=[
                ('genres', models.CharField(blank=True, max_length=300)),
                ('id', models.CharField(max_length=300, primary_key='True', serialize=False)),
                ('original_title', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField()),
                ('fantasy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.fantasy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.movielist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
