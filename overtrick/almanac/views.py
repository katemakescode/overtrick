from django.shortcuts import render

from .models import Session


def index(request):
    return render(request, 'session_list.html', context={'club': 'Wellington'})


def detail(request, session_id):
    session = Session.objects.get(pk=session_id)
    return render(
        request,
        'session_detail.html',
        context={'session': session}
    )
