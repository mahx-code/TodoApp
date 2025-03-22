"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from todoManager.views import addTodo, home, editTodo, deleteTodo, completedTodo

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("getTodoPage", TemplateView.as_view(template_name="addTodoPage.html"), name="getTodoPage"),
    path("add-todo", addTodo, name="add-todo"),
    path("", home, name='home'),
    path("edit-todo/<int:todo_id>/", editTodo, name="edit-todo"),
    path("delete-todo/<int:todo_id>/", deleteTodo, name="delete-todo"),
    path("complete-todo/<int:todo_id>/", completedTodo, name="complete-todo"),
]

# model(orm)
# , view, urls, forms, templates