# Generated by Django 5.1.2 on 2024-10-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_rename_grades_grade_grade_alter_animematerials_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='sum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]