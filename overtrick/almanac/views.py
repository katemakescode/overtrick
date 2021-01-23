from django.http import HttpResponse


def index(request):
    return HttpResponse("Session listing goes here.")
