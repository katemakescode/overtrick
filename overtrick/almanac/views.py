from django.shortcuts import get_object_or_404, render

from .models import Session


def list(request):
    return render(
        request,
        'session_list.html',
        {'sessions': Session.objects.order_by('-date')[:3]}
    )


def detail(request, session_id):
    return render(
        request,
        'session_detail.html',
        {'session': get_object_or_404(Session, pk=session_id)}
    )
