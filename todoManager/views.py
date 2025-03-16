from django.shortcuts import render, redirect
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