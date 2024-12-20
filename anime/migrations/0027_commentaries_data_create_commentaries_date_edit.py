# Generated by Django 5.1.2 on 2024-11-02 23:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0026_remove_animematerials_commentaries'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaries',
            name='data_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentaries',
            name='date_edit',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
