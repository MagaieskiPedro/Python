from rest_framework.permissions import BasePermission

class IsGestor(BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated and request.user.categoria == 'G':
            return True
        else:
            return False

class IsFuncionario(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.categoria == 'F'
    
class IsCliente(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.categoria == 'C'

class IsGestorOuFuncionario(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user.is_authenticated and request.user.categoria == 'G' or request.user.categoria == 'F':
            return True
        return obj.id == request.user.id