from django.http.response import HttpResponse

def HelloWorld(request):
    return HttpResponse('<h1>Hello World!</h1>')