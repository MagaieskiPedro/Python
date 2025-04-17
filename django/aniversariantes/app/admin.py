from django.contrib import admin
from .models import Aniversariante,Usuario
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UsuarioAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('Campos Novos', {
            'fields': ('telefone','data_nascimento','foto_perfil')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Novos', {
            'fields': ('telefone','data_nascimento','foto_perfil')
        }),
    )

admin.site.register(Aniversariante)
admin.site.register(Usuario, UsuarioAdmin)