# Generated by Django 3.2.16 on 2022-11-28 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0008_alter_project_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='approvers',
        ),
    ]