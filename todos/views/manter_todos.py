# -*- encoding: utf-8 -*-
from rest_framework import routers, serializers, viewsets
from todos.models.todo import Todo
from todos.views.TodoSerializer import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    Classe que define o retorno (modelo) a ser utilizado na API e 
    mapeia os métodos HTTP a serem utilizados. 
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer