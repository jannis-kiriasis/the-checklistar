# Generated by Django 3.2.16 on 2022-11-22 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approver_department', models.CharField(max_length=80)),
                ('approval_date', models.DateField(blank=True, null=True)),
                ('approval_due_by', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Not approved'), (1, 'Approved')], default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='approvers',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ProjectApprover',
        ),
        migrations.AddField(
            model_name='projectapproval',
            name='approver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='approvers', to='project_management.userprofile'),
        ),
        migrations.AddField(
            model_name='projectapproval',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='approvals', to='project_management.project'),
        ),
    ]
