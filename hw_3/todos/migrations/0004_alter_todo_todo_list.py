# Generated by Django 5.0.2 on 2024-03-06 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todolist_todo_todo_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='todos.todolist'),
        ),
    ]