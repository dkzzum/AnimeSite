# Generated by Django 5.1.2 on 2024-10-25 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10.0)),
                ('sum', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AnimeMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('commentaries', models.IntegerField(blank=True, default=0)),
                ('category', models.ManyToManyField(related_name='category', to='anime.category')),
                ('grade', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grade', to='anime.grade')),
            ],
        ),
    ]
