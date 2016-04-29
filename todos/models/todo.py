from django.db import models

class Todo(models.Model):
    descricao = models.CharField(max_length=800)
    data = models.DateField()
    
    class Meta:
        app_label = 'todos'
        db_table = 'todos'