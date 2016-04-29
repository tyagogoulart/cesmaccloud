from rest_framework import routers, serializers, viewsets
from todos.models.todo import Todo
from todos.views.TodoSerializer import TodoSerializer

# ViewSets define the view behavior.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer