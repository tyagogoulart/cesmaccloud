from django.shortcuts import render_to_response
from django.template.context import RequestContext

def AdicionaTodo(request):
   
   return render_to_response('adiciona_todo.html', locals(), context_instance=RequestContext(request))