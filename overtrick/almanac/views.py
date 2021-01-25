from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'session_list.html', context={'club': 'Wellington'})


def detail(request, session_id):
    return HttpResponse(f'Session {session_id} results go here.')
