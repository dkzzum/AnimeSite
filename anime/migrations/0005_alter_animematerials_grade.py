# Generated by Django 5.1.2 on 2024-10-25 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_alter_animematerials_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animematerials',
            name='grade',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grades', to='anime.grade'),
        ),
    ]