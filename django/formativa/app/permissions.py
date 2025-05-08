from rest_framework.permissions import BasePermission

class isGestor(BasePermission):
    def has_permission(self,request, view):
        if request.user.is_authenticated and request.user.categoria == 'G':
            return True
        return False
class isComum(BasePermission):
    def has_permission(self,request, views):
        if request.user.is_authenticated and request.user.categoria == 'C':
            return True
        return False

