# Generated by Django 3.2.16 on 2022-11-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0005_project_approvers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectapproval',
            name='status',
        ),
        migrations.AddField(
            model_name='projectapproval',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
