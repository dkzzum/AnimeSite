# Generated by Django 5.1.2 on 2024-10-25 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='grades',
            new_name='grade',
        ),
        migrations.AlterField(
            model_name='animematerials',
            name='grade',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grades', to='anime.grade'),
        ),
    ]
