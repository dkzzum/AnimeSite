# Generated by Django 5.1.2 on 2024-10-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0009_animematerials_is_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animematerials',
            old_name='content',
            new_name='description',
        ),
    ]
