# Generated by Django 5.1.2 on 2024-10-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_alter_animematerials_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='animematerials',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
