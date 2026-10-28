from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return(
                request.user
                and request.user.is_authenticated
                and (request.user.is_superuser or request.user.is_staff)
            )


class ComprasPermission (permissions.BasePermission):
    """ Permiso de Compras: No borrar compras pero si se pueden crear, listar, modificar(Reembolso) """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.method == 'DELETE':
            return False
        if request.method in permissions.SAFE_METHODS:
            return request.user.rol in ['cliente','empleado',]
        return request.user.rol == 'gerente'
    
class InventarioPermission (permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            request.user.rol in ['cliente','gerente']
        return request.user.rol == 'empleado'

class isGerente(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.method == 'PUT':
            return True
        if request.method in permissions.SAFE_METHODS:
            return request.user.rol in ['cliente','empleado']
        return request.user.rol == 'gerente'

