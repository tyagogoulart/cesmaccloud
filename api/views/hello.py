# -*- encoding: utf-8 -*-
from django.http.response import HttpResponse

def HelloWorld(request):
    """
    Método utilizado como primário para retornar 
    uma página Hello World para teste no Elastic Beanstalk.
    """
    
    return HttpResponse('<h1>Hello World!</h1>')