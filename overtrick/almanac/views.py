from django.shortcuts import render

from .models import Session


def index(request):
    return render(
        request,
        'session_list.html',
        context={'sessions': Session.objects.order_by('-date')[:3]}
    )


def detail(request, session_id):
    return render(
        request,
        'session_detail.html',
        context={'session': Session.objects.get(pk=session_id)}
    )
