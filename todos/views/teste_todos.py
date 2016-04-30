from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todos.models.todo import Todo
from django.contrib.auth.models import User
from todos.views.TodoSerializer import TodoSerializer

class TesteCriarTodo(APITestCase):
    def setUp(self):
        self.data = {'descricao': 'teste', 'data': '30/04/2016'}
        
    def teste_criar_todo(self):
        response = self.client.post('/todos/', self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().descricao, 'teste')
        
class TesteDeletarTodo(APITestCase):
    def setUp(self):
        self.todo = Todo.objects.create(descricao='teste', data='20/05/2016')
        
    def teste_deletar_todo(self):
        response = self.client.delete('/todos/1/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TesteListarTodo(APITestCase):
    def setUp(self):
        self.todo = Todo.objects.create(descricao='teste', data='20/05/2016')
        
    def teste_listar_todo(self):
        response = self.client.get('/todos/', args=[self.todo.id])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.get().descricao, 'teste')
        
    def teste_listar_todos_all(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TesteModificarTodo(APITestCase):
    def setUp(self):
        self.todo = Todo.objects.create(descricao='teste', data='20/05/2016')
        
    def teste_modificar_todo(self):
        response = self.client.put('/todos/1/', {'descricao': 'teste modificado', 'data': '22/05/2016'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)