from django.db import models
from django.db.models import ForeignKey, CASCADE


# Create your models here.


class Todo_List(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    isDone = models.BooleanField(default=False)
    todo_list = models.ForeignKey(Todo_List, on_delete=models.CASCADE, null=True)
