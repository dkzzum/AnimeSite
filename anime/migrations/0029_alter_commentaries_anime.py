# Generated by Django 5.1.2 on 2024-11-03 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0028_alter_commentaries_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaries',
            name='anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anime_commentaries', to='anime.animematerials'),
        ),
    ]