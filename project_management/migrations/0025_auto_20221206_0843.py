# Generated by Django 3.2.16 on 2022-12-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0024_alter_project_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectapproval',
            name='approval_due_by',
            field=models.DateField(blank=True, null=True),
        ),
    ]
