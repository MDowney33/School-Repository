from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse(str(request))

def home(request):
    return HttpResponse('h')

def about(request):
    return HttpResponse('h')

def blog(request):
    return HttpResponse('h')