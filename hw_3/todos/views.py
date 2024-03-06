from django.shortcuts import render, redirect
from .form import CUForm, ListForm
from .models import Todo, Todo_List


# Create your views here.
def main(request):
    todo = Todo_List.objects.all()
    context = {'todo': todo}
    return render(request, 'main.html', context)


def showlist(request, pk):
    listT = Todo_List.objects.get(id=pk)
    listtodo = listT.todo_set.all()
    context = {'todo': listtodo, "list": listT}
    return render(request, 'list.html', context)


def createList(request):
    todo = Todo_List()
    form = ListForm(request.POST, instance=todo)
    context = {'form': form}
    return render(request, 'form.html', context)


def updateList(request, pk):
    todo = Todo_List.objects.get(id=pk)
    form = ListForm(instance=todo)

    return render(request, 'update.html', {'form': form, 'todo': todo})


def updateListTotal(request, pk):
    todo = Todo_List.objects.get(id=pk)

    if request.method == 'POST':

        form = ListForm(request.POST or None, instance=todo)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = CUForm(instance=todo)
    return render(request, '/updateAction/' + pk, {'form': form})


def createListTotal(request):
    todo = Todo_List()
    form = ListForm(request.POST, instance=todo)
    if form.is_valid():
        todo = Todo_List()
        todo.title = form.cleaned_data['title']
        todo.description = form.cleaned_data['description']
        todo.save()
        print("Created TODO")
    return redirect("/")


def doneList(request, pk):
    todo = Todo_List.objects.get(id=pk)
    todo.delete()
    return redirect("/")


def createAction(request, pk):
    todo = Todo()
    todolist = Todo_List.objects.get(id=pk)
    form = CUForm(request.POST, instance=todo)
    context = {'form': form, 'todolist': todolist}
    return render(request, 'todoform.html', context)


def updateAction(request, pk):
    todo = Todo.objects.get(id=pk)
    form = CUForm(instance=todo)

    return render(request, 'update.html', {'form': form, 'todo': todo})


def create(request, pk):
    todo = Todo()
    todolist = Todo_List.objects.get(id=pk)
    form = CUForm(request.POST, instance=todo)
    if form.is_valid():
        todo = Todo()
        todo.title = form.cleaned_data['title']
        todo.description = form.cleaned_data['description']
        todo.due_date = form.cleaned_data['due_date']
        todo.isDone = False
        todo.todo_list = todolist
        todo.save()
        print("Created TODO")
    return redirect('/showList/' + pk)


def done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')


def update(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':

        form = CUForm(request.POST or None, instance=todo)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = CUForm(instance=todo)
    return redirect('/showList/' + pk)
