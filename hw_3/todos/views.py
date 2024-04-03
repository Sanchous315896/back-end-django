from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import CUForm, ListForm, AUTHUserForm, REGUserForm
from .models import Todo, Todo_List


@login_required
def main(request):
    todo = Todo_List.objects.filter(user=request.user)
    user = request.user
    context = {'todo': todo, 'user': user}
    return render(request, 'main.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('auth/')


def reg(request):
    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #
    #     print(form.data.get("username"))
    #     print(form.data.get("password"))

    form = REGUserForm(request.POST)
    context = {'form': form}
    return render(request, 'registration.html', context)


def registrate(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save
        return redirect('/auth/')  # Перенаправляем пользователя на страницу входа после успешной регистрации

    return redirect("/reg/")


def auth(request):
    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #
    #     print(form.data.get("username"))
    #     print(form.data.get("password"))

    form = AUTHUserForm(request.POST)
    context = {'form': form}
    return render(request, 'authorization.html', context)


def authorize(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return redirect("/reg/")


def showlist(request, pk):
    listT = Todo_List.objects.get(id=pk)
    listtodo = listT.todo_set.all()
    context = {'todo': listtodo, "list": listT}
    return render(request, 'list.html', context)


@login_required
def createList(request):
    todo = Todo_List()
    form = ListForm(request.POST, instance=todo)
    context = {'form': form}
    return render(request, 'form.html', context)


def updateList(request, pk):
    todo = Todo_List.objects.get(id=pk)
    form = ListForm(instance=todo)

    return render(request, 'update.html', {'form': form, 'todo': todo})


@login_required
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


@login_required
def createListTotal(request):
    todo = Todo_List()
    form = ListForm(request.POST, instance=todo)
    if form.is_valid():
        todo = Todo_List()
        todo.title = form.cleaned_data['title']
        todo.description = form.cleaned_data['description']
        todo.user = request.user
        todo.save()
        print("Created TODO")
    return redirect("/")


@login_required
def doneList(request, pk):
    todo = Todo_List.objects.get(id=pk)
    todo.delete()
    return redirect("/")


@login_required
def createAction(request, pk):
    todo = Todo()
    todolist = Todo_List.objects.get(id=pk)
    form = CUForm(request.POST, instance=todo)
    context = {'form': form, 'todolist': todolist}
    return render(request, 'todoform.html', context)


@login_required
def updateAction(request, pk):
    todo = Todo.objects.get(id=pk)
    form = CUForm(instance=todo)

    return render(request, 'update.html', {'form': form, 'todo': todo})


@login_required
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


@login_required
def done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')


@login_required
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
