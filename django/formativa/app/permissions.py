from rest_framework.permissions import BasePermission

class isGestor(BasePermission):
    def has_permission(self,request):
        if request.user.is_authenticated and request.user.categoria == 'G':
            return True
        return False
class isComum(BasePermission):
    def has_permission(self,request):
        if request.user.is_authenticated and request.user.categoria == 'C':
            return True
        return False
class isGestorOuComum(BasePermission):
    def has_object_permission(self,request,obj):
        if request.user.is_authenticated and request.user.categoria == 'C' or request.user.categoria == 'G':
            return True
        return obj.id == request.user.id