from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.decorators import feature_required


@login_required
@feature_required('ENABLE_NOTIFICATIONS')
def lista(request):
    return render(request, 'notificaciones/lista.html', {'notificaciones': request.user.notificaciones.all()[:20]})


@login_required
@feature_required('ENABLE_NOTIFICATIONS')
def marcar_leidas(request):
    if request.method == 'POST':
        request.user.notificaciones.filter(leida=False).update(leida=True)
    return redirect('notificaciones:lista')
