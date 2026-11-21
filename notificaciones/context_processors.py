def pendientes(request):
    if request.user.is_authenticated:
        return {'notificaciones_pendientes': request.user.notificaciones.filter(leida=False).count()}
    return {}
