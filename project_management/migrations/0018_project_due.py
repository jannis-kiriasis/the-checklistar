# Generated by Django 3.2.16 on 2022-11-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0017_alter_projectapproval_approver'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]