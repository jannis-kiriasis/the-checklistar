# Generated by Django 3.2.16 on 2022-12-06 08:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0023_alter_project_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]