# Generated by Django 3.2.16 on 2022-12-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_alter_notification_to_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='extra_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
