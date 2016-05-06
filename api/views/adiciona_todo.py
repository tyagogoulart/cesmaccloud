# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def AdicionaTodo(request):
    """
    Método de teste da API que retorna uma página para adicionar uma TODO.
    """
    
   
    return render_to_response('adiciona_todo.html', locals(), context_instance=RequestContext(request))