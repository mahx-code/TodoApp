from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.

def addTodo(request):
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        print(title, description)

        Todo.objects.create(
            title=title, 
            description=description
        )

        return redirect('home')
    
    return render(request, template_name='addTodoPage.html')






def home(request):
    todos = Todo.objects.all()
    return render(request, template_name="index.html", context={"todos": todos})





def editTodo(request, todo_id):
    todo = get_object_or_404(Todo, id = todo_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        todo.title = title
        todo.description = description
        todo.save()

        return redirect('home')
    else:
        return render(request, template_name="editTodo.html", context={"todo": todo})
    



def deleteTodo(request, todo_id):
    todo = get_object_or_404(Todo, id = todo_id)
    todo.delete()
    return redirect('home')


def completedTodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')
