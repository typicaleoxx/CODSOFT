# Generated by Django 5.0.1 on 2024-02-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='desciption',
            field=models.CharField(default=None, max_length=200),
        ),
    ]