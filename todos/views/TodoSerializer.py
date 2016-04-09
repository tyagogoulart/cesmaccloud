from rest_framework import routers, serializers, viewsets
from todos.models.todo import Todo

# Serializers define the API representation.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'descricao', 'data')