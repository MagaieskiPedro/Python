from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Produto
# Register your models here.
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Novos Campos',{'fields':('categoria',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('categoria',)}),
    )
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Produto)