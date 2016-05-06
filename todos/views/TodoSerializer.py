# -*- encoding: utf-8 -*-
from rest_framework import routers, serializers, viewsets
from todos.models.todo import Todo

# Serializers define the API representation.
class TodoSerializer(serializers.ModelSerializer):
    """
    Classe Serializadora, que determina o modelo e os campos
    a serem utilizados pela API.
    """
    
    class Meta:
        model = Todo
        fields = ('id', 'descricao', 'data')
