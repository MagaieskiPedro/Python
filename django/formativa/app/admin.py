from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Professor,Ambiente,Disciplina,Usuario
# Register your models here.
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Novos campos',{'fields': ('categoria',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('categoria',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Professor)
admin.site.register(Ambiente)
admin.site.register(Disciplina)