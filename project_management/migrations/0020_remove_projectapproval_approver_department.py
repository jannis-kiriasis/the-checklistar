# Generated by Django 3.2.16 on 2022-12-01 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0019_alter_project_due'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectapproval',
            name='approver_department',
        ),
    ]
