# Generated by Django 3.2.16 on 2022-12-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0022_auto_20221206_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due',
            field=models.DateField(null=True),
        ),
    ]