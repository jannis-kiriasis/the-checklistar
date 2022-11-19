# Generated by Django 3.2.16 on 2022-11-19 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectApprover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approver_department', models.TextField()),
                ('approver', models.CharField(max_length=80)),
                ('approval_date', models.DateTimeField()),
                ('approval_due_by', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'Not approved'), (1, 'Approved')], default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='approvers', to='project_management.project')),
            ],
            options={
                'ordering': ['approval_date', 'project'],
            },
        ),
    ]
