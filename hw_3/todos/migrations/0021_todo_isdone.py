# Generated by Django 5.0.2 on 2024-03-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0020_remove_todo_isdone'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]