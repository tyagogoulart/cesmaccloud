from django.db import models

class Todo(models.Model):
    """
    Modelo que define os campos da tabela todos no banco de dados
    e que serão utilizados na API.
    """
    descricao = models.CharField(max_length=800)
    data = models.CharField(max_length=10)
    
    class Meta:
        app_label = 'todos'
        db_table = 'todos'